from fastapi import FastAPI

from app.database.database import Base, engine

# Import models so SQLAlchemy registers them
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Smart Health Monitoring API",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "message": "Smart Health Monitoring API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }