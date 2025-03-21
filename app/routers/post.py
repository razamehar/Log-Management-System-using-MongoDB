from fastapi import APIRouter, HTTPException, Depends, status
from pymongo.collection import Collection
from app.utils.database import get_db
from app.utils.schema import PostBase


post_router = APIRouter()

def get_collection() -> Collection:
    connection = get_db()
    db = connection.logs_db
    return db.log_entries


@post_router.post("/document/")
async def post_one(document: PostBase, collection: Collection = Depends(get_collection)):
    try:
        document_dict = document.dict()
        result = collection.insert_one(document_dict)
        return {"message": "Document inserted", "id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inserting document: {str(e)}")


@post_router.post("/documents/")
async def post_many(documents: list[PostBase], collection: Collection = Depends(get_collection)):
    try:
        documents_dict = [document.dict() for document in documents]
        result = collection.insert_many(documents_dict)
        return {"message": "Documents created", "document_ids": [str(doc_id) for doc_id in result.inserted_ids]}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
