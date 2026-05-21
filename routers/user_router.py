from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import UserCreate, UserResponse, LoginRequest
import bcrypt

router = APIRouter(prefix="/users", tags=["Users"])

users_db = []
id_counter = 1

@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def new_user(user_input: UserCreate):
    global id_counter
    for u in users_db:
        if u["email"] == user_input.email:
            raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    created_user = {
        "id": id_counter,
        "username": user_input.username,
        "email": user_input.email,
        "password": user_input.password,
        "active_status": True
    }   
    users_db.append(created_user)
    id_counter += 1
    return created_user

@router.get("/users/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(user_id: int):
    for u in users_db:
        if u["id"] == user_id:
            return u
            
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@router.post("/login", status_code=status.HTTP_200_OK)
def login(login_input: LoginRequest):
    for u in users_db:
        if u["email"] == login_input.email and u["password"] == login_input.password:
            return {"message": "Login realizado com sucesso!", "username": u["username"]}
            
    raise HTTPException(status_code=401, detail="E-mail ou senha incorretos")