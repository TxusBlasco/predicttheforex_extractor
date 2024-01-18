from fastapi import FastAPI
from core.infrastructure.controllers.extractor import extraction


app = FastAPI()
app.include_router(extraction)
