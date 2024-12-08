from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


engine = create_engine("sqlite:///taskmanager.db", echo=True)  #движок указав пусть в БД - 'sqlite:///taskmanager.db'
SessionLocal = sessionmaker(bind=engine) # и локальная сессия

class Base(DeclarativeBase): # Создайте базовый класс Base для других моделей, наследуясь от DeclarativeBase
    pass


class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    age=Column(Integer)