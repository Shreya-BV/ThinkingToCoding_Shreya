# Count Vowels in a Word
## Task- Ask the user to enter a word or a sentence,then count and display the number of vowels in the input.  Example-   Input: "Hello World"    Output: 3 vowels
# Task given (today)
## Task 1:Learn all the basic GitHub commands using VS / VS Code.

## Task 2:Configure database values like DB URL, DB name, and required APIs.
Store them in a config file and use them whenever needed.
Also learn:
* How to create a .env file
* How to store values in .env
* How to call environment variables in the project
  
# WHAT I LEARNED FROM TASK 1
Task 1: Learn basic GitHub commands using VS / VS Code

From Task 1, I learned how to use Git and GitHub for version control using VS Code / Git Bash.

Key things I learned:

How to initialize Git in a project using git init

How to check file status using git status

How to add files to Git tracking using git add

How to save project versions using git commit

How to configure Git username and email

How to create a GitHub repository

How to connect a local project to GitHub

How to push code to GitHub using git push

How to verify commits locally and on GitHub

# WHAT I LEARNED FROM TASK 2
Task 2: Configure database values using config and .env

From Task 2, I learned how to securely manage configuration values instead of hardcoding them in code.

Key things I learned:

What environment variables are

How to create a .env file

How to store database values like:

Database URL

Database name

Collection name

How to install and use python-dotenv

How to read environment variables using os.getenv()

How to create a config.py file to manage configuration

How to reuse configuration values across the project

Why .env files should not be uploaded to GitHub



# Code Summary
1.The program starts by importing required libraries for MongoDB connectivity, error handling, and date-time operations.

2.It establishes a connection to the local MongoDB server using MongoClient.

3.A ping command is used to verify that MongoDB is running before performing any database operations.

4.The program accesses (or creates) a database named vowels and a collection named vowel_data.

5.It prompts the user to enter a word or sentence as input.

6.Input validation is performed to ensure that the user does not submit an empty value.

7.A predefined set of vowels is used to handle both uppercase and lowercase characters.

8.The program iterates through each character in the input string and counts vowels using conditional checks.

9,The total vowel count is displayed to the user.

10.The current date and time are captured using the datetime module to track when the data is created.

11.The input, vowel count, and timestamp are stored together as a document in MongoDB.

12.Exception handling is implemented to handle MongoDB connection failures, invalid input errors, and unexpected runtime issues.

13.User-friendly messages are displayed for both successful execution and error scenarios.
# Python Code
~~~Python
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from datetime import datetime

try:
    client = MongoClient("mongodb://localhost:27017/")
    client.admin.command('ping')

    db = client["internship_db"]
    collection = db["vowel_data"]

    user_input = input("Enter a word or sentence: ")

    if user_input == "":
        raise ValueError("Input cannot be empty")

    vowels = "aeiouAEIOU"
    count = 0
    for char in user_input:
        if char in vowels:
            count += 1

    print(f"{count} vowels")

    created_time = datetime.now()

    data = {
        "input": user_input,
        "vowel_count": count,
        "created_at": created_time
    }

    collection.insert_one(data)

    print("Data stored in MongoDB successfully!")

except ConnectionFailure:
    print("Error: MongoDB is not running.")

except ValueError as ve:
    print("Input Error:", ve)

except Exception as e:
    print("Unexpected Error:", e)
~~~

# What I Learned
Learned how to take dynamic user input and process strings in Python.

Understood how to implement loop and conditional logic to count vowels in a sentence.

Learned how to handle both uppercase and lowercase characters using a predefined vowel set.

Gained hands-on experience connecting Python to MongoDB using the PyMongo library.

Learned how MongoDB databases and collections are created and accessed programmatically.

Understood how to store application data in MongoDB using document-based storage.

Learned how to capture and store timestamps using Python’s datetime module.

Implemented exception handling to manage database connection issues and invalid user input.

Learned how to make a program more robust by preventing crashes using try and except.

Gained basic understanding of backend data persistence concepts.
# Execution Screenshot


<img width="927" height="116" alt="Screenshot 2026-02-15 194624" src="https://github.com/user-attachments/assets/78c1ee55-15c7-4d70-b92d-fd0dfb084b71" />



<img width="929" height="116" alt="Screenshot 2026-02-15 194718" src="https://github.com/user-attachments/assets/25cfd602-737b-4a1e-96c7-111aff647966" />



<img width="918" height="93" alt="Screenshot 2026-02-15 194734" src="https://github.com/user-attachments/assets/6cac227a-a3b8-4c4f-93a3-68fad63a2281" />






<img width="456" height="318" alt="Screenshot 2026-02-15 195155" src="https://github.com/user-attachments/assets/9a8bfdc1-a558-4fa1-89fe-bdf00034c9a2" />










