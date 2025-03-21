from fastapi import APIRouter, HTTPException, Depends, Request
from pymongo.collection import Collection
from app.utils.database import get_db


update_router  = APIRouter()

def get_collection() -> Collection:
    connection = get_db()
    db = connection.logs_db
    return db.log_entries


@update_router.patch("/document/{event_id}")
def update_one(event_id: str, updated_fields: dict, collection: Collection = Depends(get_collection)):
    try:
        doc = collection.find_one({"event_id": event_id})
        if doc:
            update_operation = { '$set' : updated_fields}
            collection.update_one({"event_id": event_id}, update_operation)
            return {"message": "Document updated", "document": updated_fields}
        else:
            raise HTTPException(status_code=404, detail="Document not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to update the document: {e}")