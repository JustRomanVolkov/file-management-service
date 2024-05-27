from fastapi import APIRouter, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.responses import StreamingResponse
from ..services.file_service import FileService
from ..core.celery_app import process_file
from ..models.file import FileMetadata
from datetime import datetime
from bson import ObjectId

router = APIRouter()


@router.post("/files/")
async def create_file(user_id: str, file: UploadFile):
    file_metadata = FileMetadata(user_id=user_id, filename=file.filename, upload_date=datetime.now())
    file_id = await FileService.create_file(file_metadata, await file.read())
    return {"file_id": file_id}


@router.get("/files/{file_id}")
async def get_file(file_id: str):
    try:
        file_metadata = await FileService.get_file(file_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not file_metadata:
        raise HTTPException(status_code=404, detail="File not found")
    return file_metadata


@router.put("/files/{file_id}")
async def update_file(file_id: str, file_metadata: FileMetadata):
    await FileService.update_file(file_id, file_metadata)
    return {"status": "File updated"}


@router.delete("/files/{file_id}")
async def delete_file(file_id: str):
    await FileService.delete_file(file_id)
    return {"status": "File deleted"}


@router.post("/files/{file_id}/process")
async def process_file_endpoint(file_id: str, background_tasks: BackgroundTasks):
    try:
        ObjectId(file_id)  # проверка корректности ObjectId
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid file_id")

    background_tasks.add_task(process_file.delay, file_id)
    return {"status": "File processing started"}


@router.get("/files/{file_id}/download")
async def download_file(file_id: str):
    file_data = await FileService.download_file(file_id)
    if not file_data:
        raise HTTPException(status_code=404, detail="File not found")

    return StreamingResponse(file_data, media_type="application/octet-stream",
                             headers={"Content-Disposition": f"attachment; filename={file_data.filename}"})
