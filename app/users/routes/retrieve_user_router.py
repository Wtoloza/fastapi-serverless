from uuid import UUID

from fastapi import Path, Depends

from app.users.routes.base_user_router import user_router
from app.users.models import User, UserRead

from app.users.dependencies import get_user


@user_router.get(
    path="/{id}",
    response_model=UserRead
)
def retrieve_user(
    id: UUID = Path(...),
    user: User = Depends(get_user)
):
    return user
