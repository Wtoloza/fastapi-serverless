from uuid import UUID
from fastapi import Body, Depends, HTTPException

from app.users.routes.base_user_router import user_router
from app.users.models import User, UserUpdate, UserRead
from app.users.dependencies import get_user

from app.core.db import Session, get_session


@user_router.patch(
    path="/{id}",
    response_model=UserRead
)
def update_user(
    id: UUID,
    data: UserUpdate = Body(...),
    user: User = Depends(get_user),
    session: Session = Depends(get_session)
):
    user_data = data.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(user, key, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
