from app.users.routes.base_user_router import user_router


@user_router.delete(
  path="/"
)
def delete_user():
  pass