import openai
from classes import *
import json

with open("data.json", "r") as f:
    data = json.load(f)

myApiKey = data["myApiKey"]

openai.api_key = myApiKey

print("---------------------------------------\n")
print("List of all registered clients:\n")

for company in Company.companyList:
    print(f"- {company.name}")

print("\nWrite name of client for a summarized overview\n")

action = input("- ")

messages = [
    {"role": "system", "content": f"Your task is to summarize information about selected company such as emails from them, appointments, status, and times met. only summarize from the information i have given you. I need you to summarize key points from important emails as short as possible."},
    {"role": "user", "content": f"Only summarize information about {action}. Structure the message in a neat and tidy way"},
]

for company in Company.companyList:
    messages.append({"role": "assistant", "content": f"All emails from {company.name}: {company.emails}. status of {company.name}: {company.status}. times met with {company.name}: {company.timesMetWith}."})

gptOutput = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    messages=messages,
)

print("\n------------------------------------------------------\n")
print(gptOutput["choices"][0]["message"]["content"]), print()