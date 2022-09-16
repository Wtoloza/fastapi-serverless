from fastapi import HTTPException, status


def get_user(id: str):
    if id == "William":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="William is not valid"
        )
    return [id, True]
