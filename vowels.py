from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from datetime import datetime
from config import DB_URL, DB_NAME, COLLECTION_NAME
try:
    client = MongoClient(DB_URL)
    client.admin.command("ping")

    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    user_input = input("Enter a word or sentence: ")

    if user_input.strip() == "":
        raise ValueError("Input cannot be empty")

    vowels = "aeiouAEIOU"
    count = sum(1 for char in user_input if char in vowels)

    print(f"{count} vowels")

    collection.insert_one({
        "input": user_input,
        "vowel_count": count,
        "created_at": datetime.now()
    })

    print("Data stored in MongoDB successfully!")

except ConnectionFailure:
    print("Error: MongoDB is not running.")

except Exception as e:
    print("Unexpected Error:", e)