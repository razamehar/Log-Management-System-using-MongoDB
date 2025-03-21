from pydantic import BaseModel
from typing import Dict, Optional, Any


class Context(BaseModel):
    data: Dict[str, Any]
    retry_attempts: int


class PostBase(BaseModel):
    timestamp: str
    level: str
    event_id: str
    message: str
    source: str
    user_id: Optional[str]
    ip_address: str
    request_id: str
    context: Context
    environment: str
    host: str
    duration: str