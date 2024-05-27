from app.core.celery_app import celery_app
from bson import ObjectId
import pymongo
from gridfs import GridFS


@celery_app.task
def process_file(file_id: str):
    client = pymongo.MongoClient("mongodb://mongo:27017")
    database = client.file_database
    fs = GridFS(database)

    # Получение файла из GridFS
    file_data = fs.get(ObjectId(file_id))
    content = file_data.read()

    # Обработка файла (разворот содержимого задом наперед)
    processed_data = content[::-1]

    # Сохранение обработанного файла в GridFS с новым именем
    fs.put(processed_data, _id=ObjectId(file_id), filename=f"processed_{file_id}.txt")
    client.close()