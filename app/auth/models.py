from app import db, bcrypt #bcrypt is to hash the password before storing
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin,db.Model):
    __tableame__='users'

    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(20))
    user_email=db.Column(db.String(20),unique=True,index=True)
    user_password=db.Column(db.String(100))
    registration_date=db.Column(db.DateTime,default=datetime.now)

    @classmethod
    def create_user(cls,user,email,password):#cls is like self but for methods that are like static

        user=cls(user_name=user,
                user_email=email,
                user_password=bcrypt.generate_password_hash(password).decode('utf-8'))

        db.session.add(user)
        db.session.commit()
        return user
