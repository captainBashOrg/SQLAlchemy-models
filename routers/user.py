from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.models import *


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    task = relationship('Task', back_populates='user')


from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))

from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))

from fastapi import APIRouter
router = APIRouter(prefix='/user', tags=['user'])
@router.get('/')
async def all_user():
    pass
@router.get('/user_id')
async def user_by_id():
    pass
@router.get('/create')
async def create_user():
    pass
@router.get('/update')
async def update_user():
    pass
@router.get('/delete')
async def delete_user():
    pass

