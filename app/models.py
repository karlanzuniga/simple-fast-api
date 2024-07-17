from sqlalchemy import Column, Integer, String
from .database import Base

class YourTable(Base):
    __tablename__ = "your_table"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)