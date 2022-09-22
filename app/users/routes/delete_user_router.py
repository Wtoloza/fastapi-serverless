from uuid import UUID

from fastapi import Depends, HTTPException

from app.users.routes.base_user_router import user_router
from app.users.models import User
from app.users.dependencies import get_user

from app.core.db import Session, get_session


@user_router.delete(
    path="/{id}"
)
def delete_user(
    id: UUID,
    session: Session = Depends(get_session),
    user: User = Depends(get_user)
):
    session.delete(user)
    session.commit()
    return {"User deleted": id}
