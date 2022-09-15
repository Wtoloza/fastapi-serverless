from fastapi import Path, Depends

from app.users.routes.base_user_router import user_router

from app.users.dependencies import get_user


@user_router.put(
  path="/{id}"
)
def update_user(
  id: str = Path(...),
  user: bool = Depends(get_user)
):
  return {f"Test_update {id}": user}