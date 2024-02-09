import openai
import json
from companies import *
from art import *

with open("myApiKey.json", "r") as f:
    apiKeyData = json.load(f)

myApiKey = apiKeyData["myApiKey"]
openai.api_key = myApiKey

commands = ["start > summarize selected company info",
            "view > disply latest saved info from selected client",
            "back > return to menu",
            "help > display all commands"]

def showCommands():

    print("List of all commands:\n")
    for i in commands:
        print("-", i)
    print()

def loadSavedData(clientName):
    clientName = clientName.lower()
    try:
        with open("data.json", "r") as f:
            savedData = json.load(f)
            return savedData.get(clientName, "Client not found")
        
    except FileNotFoundError:
        return "No data file found"

def saveData(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

savedClientSumNames = []

def showSavedClientSumNames():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
            client_names = data.keys()
            savedClientSumNames.extend(client_names)

            print("\nList of all saved client summarizations:\n")
            for name in client_names:
                print("-", name)

    except FileNotFoundError:
        print("No data file found")

print("@*-----------------------------------------------------------------------------------------------------------*@")
tprint("Summarizator 2000")

showCommands()

main = True
while main:
    action = input(": ")

    if action == "help":
        showCommands()

    elif action == "view":
        showSavedClientSumNames()
        print("\nWrite the name of a client to display lates saved AI summarization (or 'back')\n")

        view = True
        while view:

            action = input(": ")
            if action.lower() == "back":
                print("\nReturned to menu\n")
                break

            savedData = loadSavedData(action)
            print("\n", savedData, "\n")

            if savedData != "Client not found":
                view = False

    elif action == "start":
        print("\nList of all registered clients:\n")

        for company in Company.companyList:
            print(f"- {company.name}")

        nameCheck = True
        while nameCheck:

            print("\nWrite the name of a registered client to display a summarized overview (or 'back')\n")

            action = input(": ")
            if action.lower() == "back":
                print("\nReturned to menu\n")
                break
            selected_company = None
            
            for company in Company.companyList:
                if action.lower() == company.name.lower():
                    selected_company = company
                    break
            
            if selected_company:

                print("\nShortening these emails:")
                for i in selected_company.emails:
                    print("\n-", i)

                print()
                print("@*------------------------*@")
                print("| Awaiting gpt response... |")
                print("@*------------------------*@")

                nameCheck = False
                messages = [
                    {"role": "user", "content": f"Summarize and shorten and extract useful key points from {selected_company.name} emails, {selected_company.name} status, number of meetings from {selected_company.name}. Structure the message neatly with new lines. Rewrite emails to be shorter and more precise"},
                    {"role": "system", "content": f"you are an assistant for the user who responds short and precise. You do not ask questions. This is the knowledge you posses:"},
                    {"role": "system", "content": f"This is the template for showing info that you must use: {selected_company.name} emails: - (insert summarized and shoren email here)- (insert summarized and shoren email here)(one line for each email.) status: number of meetings:"},
                    {"role": "system", "content": f"{selected_company.name} emails: {selected_company.emails}. {selected_company.name} status: {selected_company.status}. {selected_company.name} number of meeting with: {selected_company.numberOfMeetings}."},
                ]

                gptOutput = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    max_tokens=2048,
                    messages=messages
                )

                print("\n-----------------------------------------\n")
                print(gptOutput["choices"][0]["message"]["content"]), print()

                savingProcess = True
                while savingProcess:
                    action = input("Save response? (y/n): ")

                    if action == "y":
                        try:
                            with open("data.json", "r") as f:
                                existing_data = json.load(f)
                        except FileNotFoundError:
                            existing_data = {}

                        existing_data[selected_company.name.lower()] = gptOutput["choices"][0]["message"]["content"]

                        with open("data.json", "w") as f:
                            json.dump(existing_data, f, indent=4)
                            f.write('\n')

                        print("\nSaved successfully")
                        print("Returned to menu\n")
                        savingProcess = False

                    elif action == "n":
                        print("\nDid not save")
                        print("Returned to menu\n")
                        savingProcess = False

                    else:
                        print("Invalid input")
            else:
                print("\nInvalid client name")