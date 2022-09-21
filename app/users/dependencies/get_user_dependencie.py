from uuid import UUID
from fastapi import Depends, HTTPException, status

from app.users.models import User

from app.core.db import Session, get_session


def get_user(id: UUID, session: Session = Depends(get_session)):
    user = session.get(User, id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f'User {id} not found'
        )
    return user
