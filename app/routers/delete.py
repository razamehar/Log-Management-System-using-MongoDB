from fastapi import APIRouter, HTTPException, Depends, Request
from pymongo.collection import Collection
from app.utils.database import get_db


delete_router  = APIRouter()

def get_collection() -> Collection:
    connection = get_db()
    db = connection.logs_db
    return db.log_entries


@delete_router.delete("/document/{event_id}")
def delete_one(event_id: str, collection: Collection = Depends(get_collection)):
    try:
        doc = collection.find_one({"event_id": event_id})
        if doc:
            collection.delete_one({"event_id": event_id})
            return {"message": "Document deleted"}
        else:
            raise HTTPException(status_code=404, detail="Document not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete the document: {e}")


@delete_router.delete("/documents/")
def delete_many(collection: Collection = Depends(get_collection)):
    try:
        docs = list(collection.find())
        if docs:
            collection.delete_many({})
            return {"message": "Documents deleted"}
        else:
            raise HTTPException(status_code=404, detail="No documents found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete the documents: {e}")