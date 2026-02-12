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
