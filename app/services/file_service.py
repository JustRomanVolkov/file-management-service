from typing import Optional
from fastapi.responses import StreamingResponse
import motor.motor_asyncio
from bson import ObjectId
import gridfs
from motor.motor_asyncio import AsyncIOMotorGridFSBucket
from ..core.config import settings
from ..models.file import FileMetadata, FileInDB

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
database = client.file_database
fs_bucket = AsyncIOMotorGridFSBucket(database)


class FileService:
    @staticmethod
    async def create_file(file_metadata: FileMetadata, file_data: bytes) -> str:
        result = await database.files.insert_one(file_metadata.dict())
        file_id = result.inserted_id
        # Сохранение файла в GridFS
        await fs_bucket.upload_from_stream_with_id(file_id, file_metadata.filename, file_data)
        return str(file_id)

    @staticmethod
    async def get_file(file_id: str) -> Optional[FileInDB]:
        file_data = await database.files.find_one({"_id": ObjectId(file_id)})
        if file_data:
            file_data["id"] = str(file_data.pop("_id"))
            return FileInDB(**file_data)
        return None

    @staticmethod
    async def update_file(file_id: str, file_metadata: FileMetadata):
        await database.files.update_one({"_id": ObjectId(file_id)}, {"$set": file_metadata.dict()})

    @staticmethod
    async def delete_file(file_id: str):
        await database.files.delete_one({"_id": ObjectId(file_id)})
        # Удаление файла из GridFS
        await fs_bucket.delete(ObjectId(file_id))

    @staticmethod
    async def download_file(file_id: str):
        file_data = await fs_bucket.open_download_stream(ObjectId(file_id))
        return file_data
