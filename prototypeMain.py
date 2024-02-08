import openai
from companies import *
import json

with open("myApiKey.json", "r") as f:
    apiKeyData = json.load(f)

myApiKey = apiKeyData["myApiKey"]
openai.api_key = myApiKey

commands = ["help", "start", "view", "exit"]

def showCommands():
    print("\nList of all commands:\n")
    for i in commands:
        print("-", i)
    print()

def loadSavedData(clientName):
    clientName = clientName.lower()
    
    with open("data.json", "r") as f:
        savedData = json.load(f)
        return savedData.get(clientName, "Client not found")

def showSavedClientSum():
    print("a")

print("---------------------------------------")

showCommands()

main = True
while main:

    action = input(": ")

    if action == "help":
        showCommands()
    
    if action == "view":

        print("\nWrite name of client to see your saved AI summarization\n")

        action = input(": ")
        
        savedData = loadSavedData(action)
        print("\n", savedData, "\n")

    if action == "exit":
        break

    if action == "start":

        print("\nList of all registered clients:\n")

        for company in Company.companyList:
            print(f"- {company.name}")

        print("\nWrite name of client for a summarized overview\n")

        action = input(": ")

        selected_company = None
        for company in Company.companyList:
            if action.lower() == company.name.lower():
                selected_company = company
                break

        
        if selected_company:
            print("\nSuccess, waiting for gpt...")
            messages = [
                {"role": "user", "content": f"Summarize and shorten {selected_company.name} emails, {selected_company.name} status, number of meetings from {selected_company.name} only! (it is very important that you only write about {selected_company.name}) structure the message neatly with new lines. Rewrite the emails to be shorter and more precise"},
                {"role": "system", "content": f"you are an assistant for the user who responds short and precise. You do not ask questions. This is the knowledge you posses:"},
                {"role": "system", "content": f"This is the template for showing info that you must use: emails: - (insert summarized and shoren email here)- (insert summarized and shoren email here)(one line for each email.) status: number of meetings:"},
                {"role": "system", "content": f"{selected_company.name} emails: {selected_company.emails}. {selected_company.name} status: {selected_company.status}. {selected_company.name} number of meeting with: {selected_company.numberOfMeetings}."},
            ]

        gptOutput = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=2048,
            messages=messages
        )

        print("\n------------------------------------------------------\n")
        print(gptOutput["choices"][0]["message"]["content"]), print()

        savingProcess = True
        while savingProcess:

            action = input("Save response? (y/n): ")

            if action == "y":

                data = {
                    selected_company.name.lower(): gptOutput["choices"][0]["message"]["content"]
                }

                with open("data.json", "a") as f:
                    # f.write(json.dumps(data))
                    json.dump(data, f, indent=4)

                    print("Saved!\n")

                savingProcess = False

            elif action == "n":
                print("Not saved!\n")
                savingProcess = False

            else:
                print("invalid input")
        
        if action == "exit":
            main = False