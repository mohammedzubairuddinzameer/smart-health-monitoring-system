from fastapi import FastAPI

app = FastAPI(
    title="Smart Health Monitoring API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Smart Health Monitoring API"
    }