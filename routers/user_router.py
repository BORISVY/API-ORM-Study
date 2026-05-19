from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Usuários"])

fakedatabase = []

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def new_user(user_input: UserCreate):
    new_user = {
        "id": 1,
        "name": user_input.name,
        "email": user_input.email,
        "active_status": True}

    fakedatabase.append(new_user)
    return new_user