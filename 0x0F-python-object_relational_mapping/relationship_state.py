#!/usr/bin/python3
"""
Defines a State model.
Inherits from SQLAlchemy Base and links to MySQL table cities.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """Represents a state for a MySQL database.

    Attributes:
        id (str): The state's id.
        name (sqlalchemy.Integer): The city's name.
        cities (sqlalchemy.relationship): relationship with states
    """
    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False,
                primary_key=True, unique=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
