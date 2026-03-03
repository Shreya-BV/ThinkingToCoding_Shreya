from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime
from config import DB_URL, DB_NAME, COLLECTION_NAME

app = FastAPI()

# MongoDB connection
client = MongoClient(DB_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# 👇 THIS IS IMPORTANT
class TextInput(BaseModel):
    text: str

@app.post("/count-vowels")
def count_vowels(data: TextInput):

    user_input = data.text.strip()

    if user_input == "":
        raise HTTPException(status_code=400, detail="Input cannot be empty")

    vowels = "aeiouAEIOU"
    count = sum(1 for char in user_input if char in vowels)

    collection.insert_one({
        "input": user_input,
        "vowel_count": count,
        "created_at": datetime.now()
    })

    return {
        "input_text": user_input,
        "vowel_count": count,
        "message": "Stored in MongoDB successfully"
    }