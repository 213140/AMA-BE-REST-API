from fastapi import FastAPI

from app.db.session import engine
from app.db.base import Base
from app.api.routers.auth import router as auth_router
from app.api.routers.items import router as items_router  # NEW

def create_app() -> FastAPI:
    app = FastAPI(title="Backend REST API", version="0.3.0")

    @app.get("/health")
    def health():
        return {"status": "ok"}

    # Register routers
    app.include_router(auth_router)
    app.include_router(items_router)  # NEW

    return app


app = create_app()

# Create DB tables (for development only)
Base.metadata.create_all(bind=engine)
