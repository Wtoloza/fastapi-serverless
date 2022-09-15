from app.users.routes.base_user_router import user_router


@user_router.post(
  path="/"
)
def create_user():
  pass