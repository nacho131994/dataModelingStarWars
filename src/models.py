import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(250), nullable=False)
    name = Column(String(250))
    last_name = Column(String(250))
    password = Column(Integer)
    email = Column(String(250))


class Cards(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True)

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    card_id = Column(Integer, ForeignKey("cards.id"))


class Characters(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
  
    birth_planet = Column(Integer(), ForeignKey("planets.id") )
    card_id = Column(Integer, ForeignKey("cards.id"))


class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    gravity = Column(Integer())
    diameter = Column(Integer())
    population = Column(Integer())
    rotation_period = Column(Integer())
    orbital_period = Column(Integer())
    climate = Column(String(250))
    terrain = Column(String(250))
    card_id = Column(Integer, ForeignKey("cards.id"))



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
