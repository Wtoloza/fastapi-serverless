from fastapi import FastAPI

from app.users.routes import user_router


def get_app():
    app = FastAPI()
    app.include_router(user_router)
    return app

app = get_app()