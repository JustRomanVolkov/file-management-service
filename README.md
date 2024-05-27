# FastAPI File Service с GridFS, Celery и Docker

Этот проект представляет собой сервис на базе FastAPI для выполнения CRUD операций с файлами, их хранения в MongoDB GridFS и обработки с помощью Celery. Сервис работает в Docker контейнерах и использует Motor для асинхронных операций с MongoDB и Redis в качестве брокера для Celery.

## Возможности

* Загрузка файлов и их хранение в MongoDB GridFS.
* Выполнение CRUD операций с метаданными файлов.
* Асинхронная обработка файлов с помощью Celery.
* Docker-ориентированная настройка для простого развертывания.

## Стек технологий

* **FastAPI** - Веб-фреймворк для создания API.
* **MongoDB** - NoSQL база данных для хранения файлов и метаданных.
* **GridFS** - Спецификация MongoDB для хранения больших файлов.
* **Motor** - Асинхронный драйвер MongoDB для Python.
* **Celery** - Распределенная очередь задач для фоновой обработки.
* **Redis** - Хранилище данных в памяти, используемое как брокер для Celery.
* **Docker** - Платформа для разработки, доставки и запуска приложений.

## Начало работы

### Предварительные требования

Убедитесь, что у вас установлены:

* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Установка

1. Клонируйте репозиторий:
   ```sh
   git clone https://github.com/TheRomanVolkov/file-management-service.git
   cd file-management-service
   ```

2. Соберите и запустите Docker контейнеры:
   ```sh
   docker-compose up --build
   ```

3. Сервер FastAPI будет доступен по адресу `http://localhost:8000`.

### API Эндпоинты

#### Загрузка файла
```http
POST /files/
```
**Параметры**:
* `user_id`: ID пользователя, загружающего файл.
* `file`: Загружаемый файл.

**Ответ**:
```json
{
  "file_id": "60f8a3b4c25e4d1f8a2b9b2d"
}
```

#### Получение метаданных файла
```http
GET /files/{file_id}
```
**Параметры**:
* `file_id`: ID файла.

**Ответ**:
```json
{
  "id": "60f8a3b4c25e4d1f8a2b9b2d",
  "user_id": "test_user",
  "filename": "example.txt",
  "upload_date": "2024-05-27T14:00:00"
}
```

#### Обновление метаданных файла
```http
PUT /files/{file_id}
```
**Параметры**:
* `file_id`: ID файла.
* `file_metadata`: Метаданные файла для обновления.

**Ответ**:
```json
{
  "status": "File updated"
}
```

#### Удаление файла
```http
DELETE /files/{file_id}
```
**Параметры**:
* `file_id`: ID файла.

**Ответ**:
```json
{
  "status": "File deleted"
}
```

#### Обработка файла
```http
POST /files/{file_id}/process
```
**Параметры**:
* `file_id`: ID файла для обработки.

**Ответ**:
```json
{
  "status": "File processing started"
}
```

### Задачи Celery

Celery worker обрабатывает файл, переворачивая его содержимое задом наперед. Обработанный файл сохраняется обратно в GridFS с новым именем.

## Лицензия

Этот проект лицензирован на условиях лицензии MIT - подробности смотрите в файле [LICENSE](LICENSE).

## Автор
Волков Роман
