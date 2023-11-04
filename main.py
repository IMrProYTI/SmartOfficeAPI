from fastapi import FastAPI
from src.router import router

app = FastAPI()

router(app)