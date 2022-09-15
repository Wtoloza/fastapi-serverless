from app.users.routes.base_user_router import user_router


@user_router.put(
  path="/"
)
def update_user():
  pass