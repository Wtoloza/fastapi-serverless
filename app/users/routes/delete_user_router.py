from uuid import UUID

from fastapi import Path, Depends,HTTPException

from app.users.routes.base_user_router import user_router
from app.users.models import User
from app.users.dependencies import get_user

from app.core.db import Session, get_session


@user_router.delete(
    path="/{id}"
)
def delete_user(
    id: UUID,
    session: Session = Depends(get_session)):
    user = session.delete(User, id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f'User {id} not found'
        )
    return user