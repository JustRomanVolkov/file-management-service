FROM python:3.11-slim

# Установка переменной окружения PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED 1

# Установка рабочей директории
WORKDIR /app

# Копирование requirements.txt и установка зависимостей
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копирование остальных файлов приложения
COPY . .

# Указание точки входа в приложение
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]