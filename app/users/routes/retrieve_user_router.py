from app.users.routes.base_user_router import user_router


@user_router.get(
  path="/{id}"
)
def retrieve_user(id: str):
  pass