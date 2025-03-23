from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os
from dotenv import load_dotenv

load_dotenv()
 
app = FastAPI(
    title="JWT-authentication and authorization",
    version="1.0.0",
    summary="JWT",
    description="JWT token authentication",
    openapi_url="/api/sms/openapi.json",
    
)   

app.mount("/api/sms/", app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

mode = os.environ.get("ENVIRONMENT_MODE")

if mode == "local":
    username = os.environ.get("DB_USER")
    password = os.environ.get("DB_PASSWORD")
    port = os.environ.get("DB_PORT")
    database_name = os.environ.get("DB_DATABASE_NAME")
    SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@localhost/{database_name}"