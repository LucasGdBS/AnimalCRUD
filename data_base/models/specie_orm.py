'''module that contains the class that represents the species table in the database'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from data_base.configs.base import Base
from data_base.models.animals_orm import Animal

class Specie(Base):
    '''class that represents the species table in the database'''
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    specie_name = Column(String(50), nullable=False, unique=True)
    animals = relationship('Animal', lazy='subquery', backref='animals', cascade="all, delete-orphan")

    def __repr__(self):
        return f'{self.specie_name}'
