from configuration.config import *
from configuration.database import *
import uvicorn
import os
from dotenv import load_dotenv
from api.user.user_routes import user_router
import logging
app.include_router(user_router)

load_dotenv()
Base.metadata.create_all(bind=engine)
logging.basicConfig(filename='log.txt', level=logging.ERROR)
if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0",port=int(os.getenv('PORT')) ,reload=True)