from sqlmodel import SQLModel, Session

from app.core.db.sqlite import engine

def get_session():
    with Session(engine) as session:
        yield session