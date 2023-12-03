from data_base.models.specie_orm import Specie
from data_base.configs.connection import DBConnectionHandler
from sqlalchemy.orm.exc import NoResultFound

class SpecieRepository:
    def select_all(self):
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Specie).all()
            except NoResultFound:
                return None
            except Exception as e:
                raise e
    
    def select_by_id(self, id):
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Specie).filter(Specie.id == id).one()
            except NoResultFound:
                return None
            except Exception as e:
                raise e
    
    def select_by_name(self, name:str):
        with DBConnectionHandler() as db:
            try:
                return db.session.query(Specie).filter(Specie.specie_name == name).first()
            except NoResultFound:
                return None
            except Exception as e:
                raise e
    
    def insert(self, specie: Specie):
        with DBConnectionHandler() as db:
            try:
                db.session.add(specie)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
    
    def update(self, specie: Specie):
        with DBConnectionHandler() as db:
            try:
                db.session.query(Specie).filter(Specie.id == specie.id).update(
                    {
                        'specie_name': specie.specie_name
                    }
                )
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
    
    def delete(self, specie: Specie):
        with DBConnectionHandler() as db:
            try:
                db.session.delete(specie)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e