from pydantic import BaseModel
from datetime import datetime


class FileMetadata(BaseModel):
    user_id: str
    filename: str
    upload_date: datetime


class FileInDB(FileMetadata):
    id: str
