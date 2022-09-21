from uuid import UUID

from fastapi import Path, Depends

from app.users.routes.base_user_router import user_router

from app.users.dependencies import get_user


@user_router.delete(
    path="/{id}"
)
def delete_user(
    id: UUID = Path(...),
    user: bool = Depends(get_user)
):
    return {f"Test_delete {id}": user}
