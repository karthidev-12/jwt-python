from .user_service import *


def create_user_controller(db,user):
    
    data=get_user_byemail(db,user)
    if data is not None:
        raise error_handler(400,"Email already exist") if data.email == user.email else error_handler(400,"User already exist")
    
    
    
    return create_user_service(db,user)

def get_user_controller(page,limit,search,db):
    
    data=get_user_service(db)
    
    if page is not None and limit is not None:
        data=data[(page-1)*limit:page*limit]
        
    if search is not None:
        data=[user for user in data if search.lower() in user.email.lower()]
    return data

def update_user_controller(id,user,db):
    return update_user_service(id,user,db)

def delete_user_controller(id,db):
    return delete_user_service(id,db)

def login_user_controller(db,user):
    return login_user_service(db,user)