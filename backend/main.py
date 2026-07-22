from fastapi import FastAPI

app = FastAPI(
    title="Smart Health Monitoring API",
    description="Production-grade Health Monitoring System",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to Smart Health Monitoring API",
        "status": "running"
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }