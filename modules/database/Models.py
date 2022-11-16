from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from flask_login import LoginManager, UserMixin

Base = declarative_base()


class Users(Base, UserMixin):

    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

    def __repr__(self):
        return f'\n<Users: {self.id} | {self.name} | {self.email} | {self.password}>'

