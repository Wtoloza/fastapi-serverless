from app.users.routes.base_user_router import user_router


@user_router.delete(
  path="/{id}"
)
def delete_user(id: str):
  pass