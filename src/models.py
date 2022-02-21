import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    usernamename = Column(String(250), nullable=False)
    password = Column(Integer, primary_key=True)
    email = Column(String(30), nullable=False)

class Favorite_Characters(Base):
    __tablename__ = 'favorite_character'
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    id_characters = Column(Integer, ForeignKey("characters.id"))

class Favorite_Planets(Base):
    __tablename__ = 'favorite_planets'
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    id_planets = Column(Integer, ForeignKey("planets.id"))

class Favorite_Starships(Base):
    __tablename__ = 'favorite_starships'
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    id_starship = Column(Integer, ForeignKey("starship.id"))

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True) 
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    consumables = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)

    def to_dict(self):
        return {}


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')