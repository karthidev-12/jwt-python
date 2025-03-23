from .user_controller import *
from .user_schema import *
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends
from configuration.database import get_db
from utils.auth import verify_access_token

user_router = APIRouter(tags=["Admin"], prefix="/admin")

@user_router.post("",status_code=200,operation_id="create_admin_user",summary="Create User")
def create_user(user: CreateUser,db: Session = Depends(get_db),auth_user: str = Depends(verify_access_token)):
    return create_user_controller(db,user) 


@user_router.get("",status_code=200,operation_id="get_admin_user",summary="Get User")
def get_user(page:int = None,limit:int = None,search: str = None,db: Session = Depends(get_db),auth_user: str = Depends(verify_access_token)):
    return get_user_controller(page,limit,search,db)

@user_router.put("/{id}",status_code=200,operation_id="update_admin_user",summary="Update User")
def update_user(id:int,user: UpdateUser,db: Session = Depends(get_db),auth_user: str = Depends(verify_access_token)):
    return update_user_controller(id,user,db)

@user_router.delete("/{id}",status_code=200,operation_id="delete_admin_user",summary="Delete User")
def delete_user(id:int,db: Session = Depends(get_db),auth_user: str = Depends(verify_access_token)):
    return delete_user_controller(id,db)


@user_router.post("/login",status_code=200,operation_id="login_user",summary="Login User")
def login_user(user: LoginUser,db: Session = Depends(get_db)):
    return login_user_controller(db,user)