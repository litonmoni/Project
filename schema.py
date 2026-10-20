from pydantic import BaseModel, Field

class BaseUser(BaseModel):
     name: str
     email: str
     age: int=Field(min=18, max=150)

class UserCreateRequest(BaseUser):
    pass

class UserResponse(BaseUser):
    id: int

    class Config:
        from_attribute=True