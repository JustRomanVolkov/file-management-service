from fastapi import FastAPI
from .api import files


app = FastAPI()

app.include_router(files.router)
