from fastapi import FastAPI

from app.db.session import engine
from app.db.base import Base
from app.api.routers.auth import router as auth_router

def create_app() -> FastAPI:
    app = FastAPI(title="AMA-BE-REST-API", version="0.2.0")

    @app.get("/health")
    def health():
        return {"status": "ok"}

    app.include_router(auth_router)
    return app

app = create_app()

# Fast DB init
Base.metadata.create_all(bind=engine)
