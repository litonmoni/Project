from sqlalchemy.orm import Session
from user import User

class UserRepository:
    def create_user(self,db: Session, user_payload: User):
        db.add(user_payload)
        db.commit()
        db.refresh(user_payload)
        return user_payload

    def get_user_by_id(self, db: Session, id: int):
        db_user=db.query(User).filter(User.id == id).first()
        return db_user
    
    def get_email_by_email(self, db: Session, email: str):
        db_user=db.query(User).filter(User.email == email).first()
        return db_user

    def get_all_user(self, db:Session):
        db_user=db.query(User).all()
        return db_user

    def delete_by_email(self, db: Session, email: str):#my code
        db_user=db.query(User).filter(User.email == email).first()
        if db_user:
            db.delete(db_user)
            db.commit()   
