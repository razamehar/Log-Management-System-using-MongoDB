# Log Management System using MongoDB

This project provides an API-based system for managing log entries using **MongoDB**. It allows users to store, retrieve, update, and delete logs efficiently.

---

## Features

- **CRUD Operations**: Create, Read, Update, and Delete log entries.
- **FastAPI Integration**: A robust and scalable API backend.
- **MongoDB Storage**: Uses MongoDB for structured and unstructured log storage.
- **Schema Validation**: Ensures data integrity with Pydantic.
- **Error Handling**: Proper HTTP exception handling for API endpoints.

---

## Tools & Technologies

- **MongoDB** - NoSQL Database for log storage
- **FastAPI** - Web framework for the API
- **Postman** - API testing tool
- **Pydantic** - Data validation and schema definition
- **Dotenv** - Environment variable management

---

## API Endpoints

| Method  | Endpoint               | Description                           |
|---------|------------------------|---------------------------------------|
| **GET**  | `/document/{event_id}`  | Retrieve a log entry by event ID     |
| **GET**  | `/documents/`           | Retrieve all log entries             |
| **POST** | `/document/`            | Insert a single log entry            |
| **POST** | `/documents/`           | Insert multiple log entries          |
| **DELETE** | `/document/{event_id}` | Delete a log entry by event ID       |
| **DELETE** | `/documents/`         | Delete all log entries               |
| **PATCH**  | `/document/{event_id}` | Update specific fields of a log entry |


## Running the Project

### Prerequisites
- Python 3.11
- MongoDB Installed & Running
- Virtual Environment (optional but recommended)

## Installation
```bash
    # Clone the repository
    git clone https://github.com/your-username/mongoDB-log-system.git
    
    # Navigate to the project directory
    cd mongoDB-log-system
    
    # Create a virtual environment
    python -m venv venv
    
    # Activate virtual environment
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    
    # Install dependencies
    pip install -r requirements.txt
```

##  Start the FastAPI Server
```bash
    uvicorn main:app --reload
```

## Testing with Postman
- Open Postman
- Import the API endpoints listed above
- Test CRUD operations by sending requests

## Environment Variables (.env file)
```markdown
| Variable   | Description                  | Example            |
|------------|------------------------------|--------------------|
| `USER`     | MongoDB username             | your_mongodb_user |
| `PASSWORD` | MongoDB password             | your_mongodb_password |
| `HOST`     | Database host address        | localhost |
```

## License
This project is licensed under the Raza Mehar License. For further details, refer to the LICENSE.md file.

## Contact
If you have any questions or need clarification, feel free to reach out to Raza Mehar at raza.mehar@gmail.com.