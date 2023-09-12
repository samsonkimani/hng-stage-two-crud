from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()



class User(Base):
    __tablename__ = 'users'

    id = Column(String(60), primary_key=True)
    f_name = Column(String(255))
    l_name = Column(String(255))
    email = Column(String(255))
