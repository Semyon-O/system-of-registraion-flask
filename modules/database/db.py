import sqlite3 as sql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
# from Models import Users

engine = create_engine('sqlite:///users.db')
DBSession: sessionmaker = sessionmaker(bind=engine)

session: Session = DBSession()


