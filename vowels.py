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
