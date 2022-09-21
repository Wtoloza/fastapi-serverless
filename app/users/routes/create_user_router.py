from fastapi import Body, Depends, HTTPException

from app.users.routes.base_user_router import user_router
from app.users.models import User, UserCreate, UserRead
from app.core.db import Session, get_session


@user_router.post(
    path="/",
    response_model=UserRead
)
def create_user(
    user: UserCreate = Body(...),
    session: Session = Depends(get_session)
):
    try:
        user = User(**user.dict())
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
