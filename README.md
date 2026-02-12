# Count Vowels in a Word
## Task- Ask the user to enter a word or a sentence,then count and display the njumber of vowels in the input.  Example-   Input: "Hello World"    Output: 3 vowels

# Logic Summary
1.Accept input (word/sentence) from the user.

2.Define a string containing all vowels (aeiouAEIOU).

3.Initialize a counter variable to 0.

4.Loop through each character in the input.

5.If the character is a vowel, increment the counter.

6.Display the total number of vowels.

7.Connect to MongoDB using MongoClient.

8.Create/connect to database (internship_db) and collection (vowel_data).

9.Store the input and vowel count as a document using insert_one()

# Code Summary
## 1️.Import Required Library  
pymongo is imported to establish a connection between Python and MongoDB.   
MongoClient is used to create a database connection instance.

## 2️.Establish Database Connection  
A connection is created using:  
MongoClient("mongodb://localhost:27017/")  
This connects the application to the local MongoDB server.  
A database named internship_db is selected (created automatically if it does not exist).  
A collection named vowel_data is accessed for storing records.

## 3️.Accept User Input  
The program prompts the user to enter a word or sentence.  
The input is stored in a variable for processing.

## 4️.Vowel Counting Logic  
A string containing all vowels (aeiouAEIOU) is defined to handle both lowercase and uppercase cases.  
A counter variable is initialized to 0.  
The program iterates through each character in the user input.  
If the character matches any vowel in the predefined string, the counter is incremented.  
After iteration, the counter holds the total number of vowels.

## 5.Display Output  
The total vowel count is displayed to the user in the required format.

## 6️.Store Data in MongoDB  
A document (dictionary format) is created containing:  
The original input  
The computed vowel count  
The document is inserted into the MongoDB collection using insert_one().

# Python Code
~~~Python
from pymongo import MongoClient

# Connect to MongoDB (local connection)
client = MongoClient("mongodb://localhost:27017/")

# Create / Connect to database
db = client["internship_db"]

# Create / Connect to collection
collection = db["vowel_data"]

# Take user input
user_input = input("Enter a word or sentence: ")

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
count = 0
for char in user_input:
    if char in vowels:
        count += 1

# Print result
print(f'{count} vowels')

# Store in MongoDB
data = {
    "input": user_input,
    "vowel_count": count
}

collection.insert_one(data)

print("Data stored in MongoDB successfully!")
~~~

