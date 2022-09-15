from fastapi import Path, Depends

from app.users.routes.base_user_router import user_router

from app.users.dependencies import get_user


@user_router.get(
  path="/{id}"
)
def retrieve_user(
  id: str = Path(...),
  user: bool = Depends(get_user)
):
  return {f"Test {id}": user}