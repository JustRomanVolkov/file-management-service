# FastAPI File Service with GridFS, Celery, and Docker
 <p>
  <a href="https://github.com/TheRomanVolkov/file-management-service/blob/main/README_en.md">English</a> | <a href="https://github.com/TheRomanVolkov/file-management-service/blob/main/README.md">Русский</a>
</p> 

This project is a FastAPI-based service for performing CRUD operations on files, storing them in MongoDB GridFS, and processing them with Celery. The service runs in Docker containers and uses Motor for asynchronous MongoDB operations and Redis as a Celery broker.

## Features

* Upload files and store them in MongoDB GridFS.
* Perform CRUD operations on file metadata.
* Process files asynchronously with Celery.
* Dockerized setup for easy deployment.

## Stack

* **FastAPI** - Web framework for building APIs.
* **MongoDB** - NoSQL database for storing files and metadata.
* **GridFS** - MongoDB specification for storing large files.
* **Motor** - Asynchronous MongoDB driver for Python.
* **Celery** - Distributed task queue for background processing.
* **Redis** - In-memory data structure store used as a broker by Celery.
* **Docker** - Platform for developing, shipping, and running applications.

## Getting Started

### Prerequisites

Ensure you have the following installed:

* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/TheRomanVolkov/file-management-service.git
   cd file-management-service
   ```

2. Build and start the Docker containers:
   ```sh
   docker-compose up --build
   ```

3. The FastAPI server will be available at `http://localhost:8000`.

### API Endpoints

#### Upload a file
```http
POST /files/
```
**Parameters**:
* `user_id`: ID of the user uploading the file.
* `file`: The file to be uploaded.

**Response**:
```json
{
  "file_id": "60f8a3b4c25e4d1f8a2b9b2d"
}
```

#### Get file metadata
```http
GET /files/{file_id}
```
**Parameters**:
* `file_id`: ID of the file.

**Response**:
```json
{
  "id": "60f8a3b4c25e4d1f8a2b9b2d",
  "user_id": "test_user",
  "filename": "example.txt",
  "upload_date": "2024-05-27T14:00:00"
}
```

#### Update file metadata
```http
PUT /files/{file_id}
```
**Parameters**:
* `file_id`: ID of the file.
* `file_metadata`: Metadata of the file to be updated.

**Response**:
```json
{
  "status": "File updated"
}
```

#### Delete a file
```http
DELETE /files/{file_id}
```
**Parameters**:
* `file_id`: ID of the file.

**Response**:
```json
{
  "status": "File deleted"
}
```

#### Process a file
```http
POST /files/{file_id}/process
```
**Parameters**:
* `file_id`: ID of the file to be processed.

**Response**:
```json
{
  "status": "File processing started"
}
```

### Celery Tasks

The Celery worker processes the file by reversing its content. The processed file is saved back to GridFS with a new name.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Volkov Roman
