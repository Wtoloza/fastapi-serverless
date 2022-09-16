from fastapi import Body

from app.users.routes.base_user_router import user_router
from app.users.models import UserCreate


@user_router.post(
    path="/"
)
def create_user(
    user: UserCreate = Body(...)
):
    return user
