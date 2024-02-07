import openai
import yaml
from classes import *

with open("token.yaml") as f:
    token_yaml = yaml.load(f, Loader=yaml.FullLoader)

openai.api_key = token_yaml['token']



print("---------------------------------------")
print()

for company in Company.companyList:
    print(f"{company.name}")

print()
print("1. Summarize info from all companies")
print("2. Summarize info from selected company")
print()

action = input("(1/2): ")

if action == "1":
    action = "all companies from the list"

if action == "2":
    print("Write company you want info from")
    print()
    action = input(": ")



messages = [
    {"role": "system", "content": "Your task is to summarize information about companies such as emails from them, appointments, what the use thinks of them and how many times the user has visited the company. only summarize from the information i have given you. I need you to summarize key points from important emails as short as possible."},
    {"role": "user", "content": f"summarize info about {action}. Structure the message in a neat and tidy way"},
    {"role": "user", "content": f"times met with wenited: {wenited.timesMetWith}, times met with amazon: {amazon.timesMetWith}"}
]

for company in Company.companyList:
    messages.append({"role": "assistant", "content": f"All emails from {company.name}: {company.emails}. status of {company.name}: {company.status}."})



gptOutput = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=2048,
    messages=messages,
)

print('--------------------------------------------------')
print(gptOutput)
print('\n\n--------------------------------------------------\n\n')
print(gptOutput["choices"][0]["message"]["content"])