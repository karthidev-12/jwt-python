from configuration.config import *
from configuration.database import *
from .user_model import *
from utils.auth import *
from utils.handlers import *
get_user_byemail =lambda db,user: db.query(User).filter(User.email == user.email).first()
getemail_byId =lambda db,id: db.query(User).filter(User.id == id).first()
def create_user_service(db,user):
    
    db_admin =User(name=user.name,email=user.email,password=string_to_base64(user.password))
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def get_user_service(db):
    
    return db.query(User).all()

def update_user_service(id,user,db):
    
 data=getemail_byId(db,id)
 if data is None:
    raise error_handler(400,"User not found")
 for key,val in user:
        if val != None :
            setattr(data, f"{key}", val)
 db.commit()
 db.refresh(data)
 return data 

def delete_user_service(id,db):
    
    data=getemail_byId(db,id)
    if data is None:
        raise error_handler(400,"User not found")
    db.delete(data)
    db.commit()
    return data

def login_user_service(db,user):
    
    access_token = create_access_token(user,"access")
    return access_token