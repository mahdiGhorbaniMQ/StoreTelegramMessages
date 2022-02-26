from sqlalchemy import *
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from model.Message import Message,Base

class DataBaseService(object):
    engine: create_engine
    Session: sessionmaker

    def __init__(self, connection_str):
        self.engine = create_engine(connection_str,
                                    isolation_level='AUTOCOMMIT')
        if not database_exists(self.engine.url):
            create_database(self.engine.url)

    def begin(self):
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    async def store_message(self, message):
        session = self.Session()
        session.add(message)
        session.commit()

    # def store_file(self, file_name):
    #     print()
    
    def get_all(self):
        session = self.Session()
        x = session.query(Message).all()
        print(x)
