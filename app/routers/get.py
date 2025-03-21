from fastapi import APIRouter, HTTPException, Depends, Request
from pymongo.collection import Collection
from app.utils.database import get_db


get_router = APIRouter()

def get_collection() -> Collection:
    connection = get_db()
    db = connection.logs_db
    return db.log_entries

def serialize_document(doc):
    if doc is not None:
        doc["_id"] = str(doc["_id"])
    return doc


@get_router.get("/document/{event_id}")
def get_one(event_id: str, collection: Collection = Depends(get_collection)):
    try:
        doc = collection.find_one({"event_id": event_id})
        if doc:
            return {"message": "Document found", "document": serialize_document(doc)}
        else:
            raise HTTPException(status_code=404, detail="Document not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch the document: {e}")

@get_router.get("/documents/")
def get_all(collection: Collection = Depends(get_collection)):
    try:
        docs = list(collection.find())
        if docs:
            return {"message": "Documents found", "documents": [serialize_document(doc) for doc in docs]}
        else:
            raise HTTPException(status_code=404, detail="No documents found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch documents: {e}")