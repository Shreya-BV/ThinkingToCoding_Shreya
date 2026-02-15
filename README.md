# Count Vowels in a Word
## Task- Ask the user to enter a word or a sentence,then count and display the number of vowels in the input.  Example-   Input: "Hello World"    Output: 3 vowels

# Logic Summary
1.Establish a connection to the local MongoDB server and verify availability.

2.Access or create the required database and collection.

3.Accept a word or sentence from the user.

4.Validate the input to ensure it is not empty.

5.Count vowels by iterating through each character in the input.

6.Display the total number of vowels.

7.Capture the current date and time.

8.Store the input, vowel count, and timestamp as a document in MongoDB.

9.Handle database connection errors, input validation errors, and unexpected exceptions.

# Code Summary
1.The program starts by importing required libraries for MongoDB connectivity, error handling, and date-time operations.

2.It establishes a connection to the local MongoDB server using MongoClient.

3.A ping command is used to verify that MongoDB is running before performing any database operations.

4.The program accesses (or creates) a database named internship_db and a collection named vowel_data.

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

client = MongoClient("mongodb://localhost:27017/")

db = client["vowels"]
collection = db["vowel_data"]

user_input = input("Enter a word or sentence: ")
vowels = "aeiouAEIOU"

count = 0
for char in user_input:
    if char in vowels:
        count += 1
print(f'{count} vowels')
data = {
    "input": user_input,
    "vowel_count": count
}

collection.insert_one(data)
print("Data stored in MongoDB successfully!")
~~~

# What I Learned
I learned how to take input from the user in Python and process it.  
understood how to use a loop to check each character in a string.  
learned how to count vowels using a simple condition check.  
understood how uppercase and lowercase letters can be handled together.  
learned how to connect Python to MongoDB using PyMongo.  
understood how a database and collection are created automatically in MongoDB.  
learned how to store data in MongoDB in document (JSON) format.  
understood the importance of storing results in a database instead of just printing them.

# Execution Screenshot


<img width="500" height="128" alt="Screenshot 2026-02-12 205727" src="https://github.com/user-attachments/assets/6f08e10b-0657-43d6-9d1f-84a0a276d0b6" />


<img width="506" height="131" alt="Screenshot 2026-02-12 205851" src="https://github.com/user-attachments/assets/e85e87d8-f7b1-4a8c-866e-16a76bc041d4" /> 
<br>
<br>
<img width="1710" height="908" alt="Screenshot 2026-02-12 210641" src="https://github.com/user-attachments/assets/f947a701-c869-4247-816a-d6e249135e4f" /> <br>









