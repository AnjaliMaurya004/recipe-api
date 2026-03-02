from pydantic import BaseModel, ConfigDict, EmailStr
from typing import List, Optional


class IngredientCreate(BaseModel):
    name: str


class RecipeCreate(BaseModel):
    name: str
    instructions: str
    ingredients: List[IngredientCreate]


class IngredientResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class RecipeResponse(BaseModel):
    id: int
    name: str
    instructions: str
    ingredients: List[IngredientResponse]

    model_config = ConfigDict(from_attributes=True)

#create user
class UserCreate(BaseModel):
    email: EmailStr
    password: str

#create user response
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)

#user login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

#token response
class Token(BaseModel):
    access_token: str
    token_type: str

#token data
class TokenData(BaseModel):
    id: Optional[int] = None