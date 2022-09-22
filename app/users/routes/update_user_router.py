from uuid import UUID
from fastapi import Path, Body, Depends,HTTPException

from app.users.routes.base_user_router import user_router
from app.users.models import User,UserBase, UserCreate, UserRead
from app.users.dependencies import get_user

from app.core.db import Session, get_session


@user_router.put(
    path="/{id}",
    response_model=UserRead
)
def update_user(
    id: UUID,
    user: User = Depends(get_user),
    data: UserCreate = Body(...),
    session: Session = Depends(get_session)
):
    if not user:
        raise HTTPException(
            status_code=404,
            detail=f'User {id} not found'
        )
    else:
        data = User(**data.dict())
        for field in  data.keys():
            user.field = data.get(str(field))
        session.add(user)
        session.commit()
        session.refresh(user)

        return user
