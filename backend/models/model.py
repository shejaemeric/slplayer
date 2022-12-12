from sqlalchemy import Column, Integer, String,ForeignKey, Table
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer,primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    telephone = Column(String)
    password = Column(String)
    fav_artist = Column(String)
    fav_style = Column(String)
    country = Column(String)
