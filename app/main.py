from app.utils.database  import get_db, close_db
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.get import get_router
from app.routers.post import post_router
from app.routers.delete import delete_router
from app.routers.update import update_router


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.on_event("startup")
def on_startup():
    connection = get_db()
    try:
        # Create a database "logs_db", if not already created
        db = connection.logs_db

        # Create a collection "log_entries", if not already created
        collection = db.log_entries
    finally:
        close_db(connection)

# Include routers for the API endpoints
app.include_router(get_router)
app.include_router(post_router)
app.include_router(delete_router)
app.include_router(update_router)

@app.get("/")
def root():
    print("Root end point accessed")
    return {"message": "This is the root dir for the logs database managed by MongoDB"}
