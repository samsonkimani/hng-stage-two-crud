from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.user import Base

class DB:
    """
    DB class
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Constructor
        """

        # user = getenv('root')
        # password = getenv('123456')
        # host = getenv('localhost')
        # db_name = getenv('hngusers')

        user = 'root'
        password = '123456'
        host = 'localhost'
        db_name = 'hngusers'

        self.__engine = create_engine(f'mysql+mysqldb://{user}:{password}@{host}/{db_name}')


    def reload(self):
        """
        Reload
        """

        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_maker)



    def add(self, obj):
        """
        Add
        """

        self.__session.add(obj)

    def save(self):
        """
        Save
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete
        """

        if obj:
            self.__session.delete(obj)
