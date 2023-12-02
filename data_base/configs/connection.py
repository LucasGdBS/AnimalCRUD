''' File that contains the class that allows connection to the database'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

class DBConnectionHandler:
    '''Class that allows connection to the database'''

    def __init__(self):
        '''Constructor method of the class'''

        self.__connection_string = config('DATABASE_URL')
        self.__engine = self.__create_database_egine()
        self.session = None

    def __create_database_egine(self):
        '''Method that creates the database engine'''
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        '''Method that returns the database engine string'''
        return self.__engine

    def __enter__(self):
        '''Method that is executed when entering a with block'''
        session_make = sessionmaker(autocommit=False, autoflush=False, bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        '''Method that is executed when exiting a with block'''
        self.session.close()
