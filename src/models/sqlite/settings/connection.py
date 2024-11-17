from sqlalchemy import create_engine

class DbConnectionHandle:
   def __init__(self):
      self.__connection_string = "sqlite:///storage.db"
      self.__engine = create_engine(self.__connection_string)
      
   def connect_to_db(self):
      self.__engine = create_engine(self.__connection_string)
      
   def get_engine(self):
      return self.__engine
      
db_connect_handle = DbConnectionHandle()
   