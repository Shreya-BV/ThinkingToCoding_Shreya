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

## Key things I learned:

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

## Key things I learned:

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
1.Import Required Libraries  
MongoClient to connect to MongoDB  
ConnectionFailure to handle database connection errors  
datetime to store the current date and time

2.Connect to MongoDB  
Connects to MongoDB running on localhost  
Uses a ping command to check if MongoDB is running

3.Select Database and Collection  
Database: internship_db  
Collection: vowel_data

4.Take User Input  
Prompts the user to enter a word or sentence  
Raises an error if the input is empty

5.Count Vowels  
Iterates through each character in the input  
Counts vowels (both uppercase and lowercase)

6.Store Data in MongoDB  
Stores the input text, vowel count, and timestamp  
Inserts the data as a document into MongoDB

7.Exception Handling  
Handles MongoDB connection errors  
Handles empty input errors  
Catches unexpected errors safely  
Handles empty input and unexpected errors


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


# Execution Screenshot


<img width="927" height="116" alt="Screenshot 2026-02-15 194624" src="https://github.com/user-attachments/assets/78c1ee55-15c7-4d70-b92d-fd0dfb084b71" />



<img width="929" height="116" alt="Screenshot 2026-02-15 194718" src="https://github.com/user-attachments/assets/25cfd602-737b-4a1e-96c7-111aff647966" />



<img width="918" height="93" alt="Screenshot 2026-02-15 194734" src="https://github.com/user-attachments/assets/6cac227a-a3b8-4c4f-93a3-68fad63a2281" />






<img width="456" height="318" alt="Screenshot 2026-02-15 195155" src="https://github.com/user-attachments/assets/9a8bfdc1-a558-4fa1-89fe-bdf00034c9a2" />


# .env file
<img width="1501" height="443" alt="Screenshot 2026-02-20 183714" src="https://github.com/user-attachments/assets/b667de0d-04f8-4152-a8d7-02f41cbdb417" />







# config.py File
<img width="1505" height="411" alt="Screenshot 2026-02-20 183846" src="https://github.com/user-attachments/assets/42907c71-27be-4da1-ae81-31dcde458888" />





# Github Repository view
<img width="1884" height="963" alt="Screenshot 2026-02-20 184050" src="https://github.com/user-attachments/assets/ce9cb830-7c87-431f-a6f8-1082ebad783f" />












# Conclusion
1. Task 1 helped me understand how to use Git and GitHub through VS Code for version control.

2. I learned how to initialize a repository, track files, commit changes, and push code to GitHub.

3. This task improved my understanding of code management and collaboration.

4. Task 2 taught me how to manage database configuration securely using environment variables.

5. I learned to create and use a .env file and a config file to store database values.

6. This helped me avoid hardcoding sensitive information and follow industry best practices.











