from celery import Celery
from .config import settings


celery_app = Celery(
    'worker',
    broker=settings.REDIS_URL,
    backend=settings.REDIS_URL
)

celery_app.conf.update(
    result_expires=3600,
)


@celery_app.task
def process_file(file_id: str):
    # Имплементация манипуляций с файлом
    pass
