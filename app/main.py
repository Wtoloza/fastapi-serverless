from fastapi import FastAPI

from app.core.db import SQLModel, engine

# Routes
from app.users.routes import user_router

# Tables
from app.users.models import User


def get_app():
    app = FastAPI()
    app.include_router(user_router)

    SQLModel.metadata.create_all(engine)
    return app


app = get_app()
