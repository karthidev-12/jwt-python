#**************************** Import Libraries *****************************#
from typing import Optional
from fastapi.security import HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.security.http import HTTPAuthorizationCredentials
from fastapi import HTTPException,status,Request





#*************************** Class Declaration ***************************#
class JWTBearer(HTTPBearer):
    """
    @param HTTPBearer:
    @return: None
    """
    async def __call__(self, request: Request) -> Optional[HTTPAuthorizationCredentials]:
        """
        @param request:
        @return: Optional[HTTPAuthorizationCredentials]
        @desc: This function is used to validate the token and return the credentials
        """
        # Get the authorization header
        authorization = request.headers.get("Authorization")

        # Get the scheme and credentials
        scheme, credentials = get_authorization_scheme_param(authorization)

        # Check if the scheme and credentials are valid
        if not (authorization and scheme and credentials):

            # Raise an exception if the credentials are not valid
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
        
        # Return the credentials
        return HTTPAuthorizationCredentials(scheme=scheme, credentials=credentials)