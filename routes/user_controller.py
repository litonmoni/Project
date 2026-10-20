from fastapi import APIRouter, Depends, status
from schema import UserCreateRequest
from database import get_db
from service import UserService
from sqlalchemy.orm import Session

router=APIRouter(
    prefix="/user"
)

@router.post("/create")
def create_user(payload: UserCreateRequest,db = Depends(get_db)):
    user_service=UserService()
    return user_service.create_user(db, payload)

@router.get("/list")
def get_all_users(db: Session=Depends(get_db)):
    service=UserService()
    return service.get_all_users(db)

@router.get("/{email}")
def get_user_by_email(email: str, db: Session=Depends(get_db)):
    service=UserService()
    return service.get_user_by_email(db,email)

@router.delete("/{email}")
def delete_user_by_email(email: str, db: Session=Depends(get_db)):
    service=UserService()
    return service.delete_by_mail(db,email)