from fastapi import Depends

from app.users.routes.base_user_router import user_router
from app.users.models import User, UserRead

from sqlmodel import select
from app.core.db import Session, get_session

@user_router.get(
    path="/",
    response_model=list[UserRead]
)
def get_users(
    session: Session = Depends(get_session)
):
    users: list[User] = session.exec(select(User)).all()
    return users
