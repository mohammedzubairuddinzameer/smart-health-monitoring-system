from fastapi import FastAPI

from app.api.v1.router import api_router
from app.db.session import Base, engine
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Health Monitoring API",
    version="1.0.0",
)

app.include_router(
    api_router,
    prefix="/api/v1"
)


@app.get("/")
def root():
    return {
        "message": "Smart Health Monitoring API"
    }