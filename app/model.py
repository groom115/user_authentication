from pydantic import BaseModel, EmailStr


class PostSchema(BaseModel):
    name: str
    clas: int


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
