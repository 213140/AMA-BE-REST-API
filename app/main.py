from fastapi import FastAPI

app = FastAPI(title="Backend REST API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}
