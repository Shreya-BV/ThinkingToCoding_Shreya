from pymongo import MongoClient

# Connect to MongoDB (local connection)
client = MongoClient("mongodb://localhost:27017/")

# Create / Connect to database
db = client["vowels"]

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