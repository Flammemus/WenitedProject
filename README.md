Prototype Main README
Project Overview

The Prototype Main project is a Python application designed to interact with OpenAI's GPT-3.5 language model to provide summarized information based on user input. It utilizes a predefined list of commands to perform actions such as summarizing information about registered companies and viewing previously saved summaries.
Setup

To run the project locally, follow these steps:

    Clone the repository to your local machine.
    Ensure you have Python installed (version 3.6 or higher).
    Install the required dependencies using pip install -r requirements.txt.
    Obtain an API key from OpenAI and store it in a JSON file named myApiKey.json in the project directory. The JSON file should have the following structure:

json

{
  "myApiKey": "YOUR_API_KEY_HERE"
}

Usage

The application offers the following commands:

    start: Initiates the process to summarize information about a selected company.
    view: Displays the latest saved summary for a selected client.
    help: Displays a list of available commands and their descriptions.

Upon starting the application, you'll be prompted to enter one of these commands. Follow the instructions to interact with the program accordingly.
Summarization Process

When using the start command, the program will list all registered companies. You'll be prompted to enter the name of a registered client. After selecting a company, the program will interact with the GPT-3.5 model to generate a summarized overview based on predefined prompts and the company's attributes.
Viewing Saved Summaries

With the view command, you can see the latest saved summaries for registered clients. Simply enter the name of the client you wish to view, and the program will display the saved summary if available.
Project Structure

The project consists of two main files:

    prototype.main: Contains the main functionality of the application, including command handling, data loading/saving, and interaction with the OpenAI GPT-3.5 model.
    companies.py: Defines the Company class and initializes fake company data used by the application.

The companies.py file contains fake company data used for demonstration purposes. Each company object includes attributes such as name, status, number of meetings, and a list of example emails.

Contributions to the project are welcome! If you have any suggestions, bug fixes, or enhancements, feel free to submit a pull request or open an issue on GitHub.

For any inquiries or support, please contact asmaskbau@gmail.com
