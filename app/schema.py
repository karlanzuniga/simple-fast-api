from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    pass

class UserResponse(UserBase):
    id: int

class config: 
    orn_mode= True