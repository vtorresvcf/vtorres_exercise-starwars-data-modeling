import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, func, DateTime
from sqlalchemy_utils import EmailType, PasswordType
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

#Instalado adicionalmente passlib y sqlalchemy_utils para implementar password y EmailType
#Importado adicionalmente func para calcular la fecha al momento actual

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    last_name = Column(String(70))
    email = Column(EmailType,nullable=False)
    password = Column(PasswordType(schemes=['pbkdf2_sha512']), nullable=False)
    date_inscription = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)
    favorites = relationship("favorite", back_populates="user")


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    heigth = Column(Integer,nullable=False)
    mass = Column(Integer,nullable=False)
    hair_color = Column(String(50),nullable=False)
    favorites = relationship("favorite", back_populates="characters")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),nullable=False)
    population = Column(Integer,nullable=False)
    rotation_period = Column(Integer,nullable=False)
    orbital_period = Column(Integer,nullable=False)
    diameter = Column(Integer,nullable=False)
    favorites = relationship("favorite", back_populates="planets")

class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey("user.id"))
    id_characters = Column(Integer, ForeignKey("characters.id"))
    id_planets = Column(Integer, ForeignKey("planets.id"))
    user = relationship("user", back_populates="favorites")
    characters = relationship("characters", back_populates="favorites")
    planets = relationship("planets", back_populates="favorites")


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
