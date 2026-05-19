from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    senha: str = Field(..., min_length=8)

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    active_status: bool = True

    class Config:
        from_attributes = True