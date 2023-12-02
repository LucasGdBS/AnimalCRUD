'''module that contains the class that represents the animals table in the database'''
from sqlalchemy import Column, Integer, String, ForeignKey
from data_base.configs.base import Base

class Animal(Base):
    '''class that represents the animals table in the database'''
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True)
    surname = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(1), nullable=False)
    specie = Column(Integer, ForeignKey('species.id'), nullable=False)

    def __repr__(self):
        return f'Animal: {self.surname} Age: {self.age} Gender: {self.gender} Specie: {self.specie}'
    