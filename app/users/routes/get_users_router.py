from app.users.routes.base_user_router import user_router


@user_router.get(
  path="/"
)
def get_users():
  pass