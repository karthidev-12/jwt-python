
from fastapi import HTTPException
import base64
def error_handler(status_code, message) -> dict:
    raise HTTPException(
        status_code=status_code, 
        detail={
            "status": status_code,
            "success": False,
            "message": message
        }
    )

def string_to_base64(input_string):
    # Encode the string to bytes
    bytes_string = input_string.encode('utf-8')
    # Encode the bytes to base64
    base64_bytes = base64.b64encode(bytes_string)
    # Convert base64 bytes back to a string
    base64_string = base64_bytes.decode('utf-8')
    return base64_string