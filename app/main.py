from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="Healthcare AI Assistant",
    version="1.0"
)

app.include_router(router)