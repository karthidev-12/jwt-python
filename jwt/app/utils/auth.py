import jwt
from datetime import datetime, timedelta
from typing import Optional
from api.user.user_model import User
import os
from dotenv import load_dotenv
import jwt
from fastapi import HTTPException, Request, status, Depends
from utils.jwt_bearer import JWTBearer
from sqlalchemy.orm import Session
from configuration.database import get_db
from utils.handlers import error_handler
load_dotenv()



def create_access_token(data: dict, token:str) -> str:
    """
    @param data: User object containing user details
    @param token: A string indicating the token type (e.g., "access")
    @return: Encoded JWT token as a string
    @desc: Create a JWT token for the user
    """
    expiry = datetime.utcnow() + timedelta(minutes=24)  # Correct indentation here
    access_token = {
        "email": data.email,
        "exp": expiry,
        "type": token
    } 
    key=os.getenv('JWT_SECRETS')
    token = jwt.encode(access_token, key=key, algorithm=os.getenv('ALGORITHM'))
    return token


def verify_access_token(token = Depends(JWTBearer()),db: Session = Depends(get_db)):
    """
    @param token: dictionary,
    @param db: database,
    @return: dictionary,
    @desc: Verify token for user
    """

    if token:
        try:
    
            decode_data = jwt.decode(token.credentials, key=os.getenv("JWT_SECRETS"), algorithms=os.getenv("ALGORITHM"))
            user_details = db.query(User).filter(
                User.email == decode_data.get('email'), User.is_deleted == False).first()
            print(decode_data.get('exp'))
            if datetime.utcfromtimestamp(decode_data.get('exp')) < datetime.utcnow():
                raise error_handler(403,"Token Expired")

            # print(user_details,"user")
            if user_details is None:
                raise error_handler(403,"You're not authorize to use")
    
            return user_details

        except jwt.ExpiredSignatureError as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail={
                    "message": "Invalid token or Access Denied",
                    "success": False
                })
        except HTTPException as e:
            raise e

        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={
                    "message": "Internal server error While verifying token",
                    "success": False
                })
    return False
