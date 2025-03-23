from configuration.database import *

from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(String, default=datetime.utcnow)
    is_deleted = Column(Boolean, default=False)
    
