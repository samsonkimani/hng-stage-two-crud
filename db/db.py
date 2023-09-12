from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from os import getenv
from models.user import Base
from dotenv import load_dotenv

load_dotenv('.env')


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

        user = getenv('USER')
        password = getenv('PASSWORD')
        host = getenv('HOST')
        db_name = getenv('DATABASE')
        port = getenv('PORT')

        # self.__engine = create_engine(f'postgresql://{user}:{password}@{host}/{db_name}')
        self.__engine = create_engine('postgres://hngusers_user:RzCBucKW90rSeoJzzeDJaCg03Hb4Fk7x@dpg-ck05infhdsdc73cvp1p0-a/hngusers')


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

    def query(self, cls):
        """
        Query
        """

        return self.__session.query(cls)
