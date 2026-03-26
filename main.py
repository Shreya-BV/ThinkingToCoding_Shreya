from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime
from config import DB_URL, DB_NAME, COLLECTION_NAME
from bson import ObjectId


# -----------------------------
# FastAPI Config
# -----------------------------
app = FastAPI(
    title="Vowel Counter API",
    description="API with ID-based CRUD and duplicate handling",
    version="2.0.0",
    contact={
        "name": "Shreya BV",
        "email": "shreyavaradaraj3131@gmail.com"
    }
)


# -----------------------------
# MongoDB Connection
# -----------------------------
client = MongoClient(DB_URL)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


# -----------------------------
# Models
# -----------------------------
class TextInput(BaseModel):
    text: str


# -----------------------------
# GET - Home
# -----------------------------
@app.get("/")
def home():
    return {"message": "API running successfully"}


# -----------------------------
# POST - Create (NO DUPLICATES)
# -----------------------------
@app.post("/count-vowels")
def count_vowels(data: TextInput):

    user_input = data.text.strip().lower()

    if user_input == "":
        raise HTTPException(status_code=400, detail="Input cannot be empty")

    # 🔥 Check duplicate
    existing = collection.find_one({"input": user_input})

    if existing:
        return {
            "status": "duplicate",
            "message": "This data already exists in the database.",
            "instruction": "Please use PUT /update-record/{id} to update the existing record.",
            "existing_id": str(existing["_id"]),
            "note": "Duplicate entries are not allowed."
        }

    vowels = "aeiouAEIOU"
    count = sum(1 for char in user_input if char in vowels)

    result = collection.insert_one({
        "input": user_input,
        "vowel_count": count,
        "created_at": datetime.now()
    })

    return {
        "status": "success",
        "message": "Record created successfully",
        "data": {
            "id": str(result.inserted_id),
            "text": user_input,
            "vowel_count": count,
            "created_at": datetime.now()
        }
    }


# -----------------------------
# GET - All Records
# -----------------------------
@app.get("/records")
def get_records(
    id: str = None,
    search: str = None,
    position: int = None   # ✅ NEW: get specific position
):

    # 🔹 If ID is provided → return single record
    if id:
        try:
            record = collection.find_one({"_id": ObjectId(id)})
        except:
            raise HTTPException(status_code=400, detail="Invalid ID")

        if not record:
            raise HTTPException(status_code=404, detail="Record not found")

        return {
            "status": "success",
            "data": {
                "id": str(record["_id"]),
                "text": record["input"],
                "vowel_count": record["vowel_count"],
                "created_at": record["created_at"]
            }
        }

    # 🔹 Query for search
    query = {}
    if search:
        query["input"] = {"$regex": search, "$options": "i"}

    # ✅ SORT: Latest first
    cursor = collection.find(query).sort("created_at", -1)

    records = []
    for record in cursor:
        records.append({
            "id": str(record["_id"]),
            "text": record["input"],
            "vowel_count": record["vowel_count"],
            "created_at": record["created_at"]
        })

    # ✅ NEW: Get specific position (like 2nd record)
    if position:
        if position <= 0 or position > len(records):
            raise HTTPException(
                status_code=400,
                detail="Invalid position value"
            )

        selected = records[position - 1]

        return {
            "status": "success",
            "mode": "single record by position",
            "position": position,
            "data": selected
        }

    return {
        "status": "success",
        "total_records": len(records),
        "records": records
    }
# -----------------------------
# PUT - Update using ID (NO DUPLICATE UPDATE)
# -----------------------------
@app.put("/update-record")
def update_record(
    id: str = None,
    old_text: str = None,
    new_text: str = None
):

    # 🔍 Validation
    if not new_text:
        raise HTTPException(status_code=400, detail="New text is required")

    new_text = new_text.strip().lower()

    if new_text == "":
        raise HTTPException(status_code=400, detail="New text cannot be empty")

    # 🔥 Prevent duplicate update
    duplicate = collection.find_one({"input": new_text})

    if duplicate:
        raise HTTPException(
            status_code=409,
            detail={
                "message": "This text already exists",
                "existing_id": str(duplicate["_id"]),
                "suggestion": "Use different text"
            }
        )

    vowels = "aeiouAEIOU"
    new_count = sum(1 for char in new_text if char in vowels)

    # -----------------------------
    # 🔹 CASE 1: Update using ID
    # -----------------------------
    if id:
        try:
            result = collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {"input": new_text, "vowel_count": new_count}}
            )
        except:
            raise HTTPException(status_code=400, detail="Invalid ID")

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Record not found")

        return {
            "mode": "updated using ID",
            "id": id,
            "updated_text": new_text,
            "vowel_count": new_count
        }

    # -----------------------------
    # 🔹 CASE 2: Update using old_text
    # -----------------------------
    elif old_text:
        old_text = old_text.strip().lower()

        result = collection.update_one(
            {"input": old_text},
            {"$set": {"input": new_text, "vowel_count": new_count}}
        )

        if result.matched_count == 0:
            raise HTTPException(
                status_code=404,
                detail="Old text not found"
            )

        return {
            "mode": "updated using old_text",
            "old_text": old_text,
            "updated_text": new_text,
            "vowel_count": new_count
        }

    # -----------------------------
    # ❌ No valid input
    # -----------------------------
    else:
        raise HTTPException(
            status_code=400,
            detail="Provide either 'id' or 'old_text' to update"
        )
# -----------------------------
# DELETE - Delete using ID
# -----------------------------
@app.delete("/delete-record/{id}")
def delete_record(id: str):

    try:
        result = collection.delete_one({"_id": ObjectId(id)})
    except:
        raise HTTPException(status_code=400, detail="Invalid ID")

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Record not found")

    return {"message": "Deleted successfully"}
