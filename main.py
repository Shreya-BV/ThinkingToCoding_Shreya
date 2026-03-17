from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime
from config import DB_URL, DB_NAME, COLLECTION_NAME


# -----------------------------
# FastAPI App Configuration
# -----------------------------
app = FastAPI(
    title="Vowel Counter API",
    description="A RESTful API built with FastAPI to count vowels in text and store results in MongoDB.",
    version="1.0.0",
    contact={
        "name": "Shreya BV",
        "email": "shreya@example.com"
    }
)


# -----------------------------
# MongoDB Connection
# -----------------------------
client = MongoClient(DB_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


# -----------------------------
# Request Model
# -----------------------------
class TextInput(BaseModel):
    text: str


# -----------------------------
# GET - Home Route
# -----------------------------
@app.get("/", tags=["System"])
def home():
    return {
        "message": "Welcome to the Vowel Counter API",
        "status": "API is running successfully"
    }


# -----------------------------
# POST - Create Record
# -----------------------------
@app.post("/count-vowels", tags=["Vowel Operations"])
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
        "message": "Data stored in MongoDB successfully"
    }


# -----------------------------
# GET - Fetch Records
# -----------------------------
@app.get("/records", tags=["Database"])
def get_records():

    records = list(collection.find({}, {"_id": 0}))

    return {
        "records": records
    }


# -----------------------------
# PUT - Update Record
# -----------------------------
@app.put("/update-record", tags=["Database"])
def update_record(old_text: str, new_text: str):

    vowels = "aeiouAEIOU"
    new_count = sum(1 for char in new_text if char in vowels)

    result = collection.update_one(
        {"input": old_text},
        {"$set": {"input": new_text, "vowel_count": new_count}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Record not found")

    return {
        "message": "Record updated successfully",
        "updated_text": new_text,
        "vowel_count": new_count
    }


# -----------------------------
# DELETE - Delete Record
# -----------------------------
@app.delete("/delete-record", tags=["Database"])
def delete_record(text: str):

    result = collection.delete_one({"input": text})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Record not found")

    return {
        "message": "Record deleted successfully"
    }