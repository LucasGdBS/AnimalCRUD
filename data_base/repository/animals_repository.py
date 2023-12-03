from data_base.models.animals_orm import Animal
from data_base.configs.connection import DBConnectionHandler
from sqlalchemy.orm.exc import NoResultFound

class AnimalsRepository:
    def select_all(self):
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Animal).all()
            except NoResultFound:
                return None
            except Exception as e:
                raise e
    
    def select_by_id(self, id):
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Animal).filter(Animal.id == id).one()
            except NoResultFound:
                return None
            except Exception as e:
                raise e
    
    def select_by_surname(self, surname):
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Animal).filter(Animal.surname == surname).all()
            except NoResultFound:
                return None
            except Exception as e:
                raise e
    
    def insert(self, animal: Animal):
        with DBConnectionHandler() as db:
            try:
                db.session.add(animal)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
    
    def update(self, animal: Animal):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Animal).filter(Animal.id == animal.id).update(
                    {
                        'surname': animal.surname,
                        'age': animal.age,
                        'gender': animal.gender,
                        'specie_id': animal.specie_id
                    }
                )
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

    def delete(self, animal: Animal):
        with DBConnectionHandler() as db:
            try:
                db.session.delete(animal)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
