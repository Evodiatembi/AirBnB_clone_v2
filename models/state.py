#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City

class State(BaseModel):
    """ State class """
    name = ""
    __tablename__ = "states"
    name = Column(String(128), null=None)
