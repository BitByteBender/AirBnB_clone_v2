#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if (getenv("HBNB_TYPE_STORAGE") != "db"):
        @property
        def cities(self):
            """
                Getter method:
                    returns a list of City objs from storage
            """
            from models.city import City
            from models import storage
            return ([c for c in storage.all(City).values()
                    if c.state_id == self.id])
