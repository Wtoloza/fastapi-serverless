from uuid import UUID
from fastapi import Path, Depends

from app.users.routes.base_user_router import user_router
from app.users.models import UserRead

from app.users.dependencies import get_user


@user_router.put(
    path="/{id}",
    # response_model=UserRead
)
def update_user(
    id: UUID = Path(...),
    user: bool = Depends(get_user)
):
    return 3
