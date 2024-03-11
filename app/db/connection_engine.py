from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL = 'sqlite:///D:/AD2/db_integration/test_db.db'

engine = create_engine(DATABASE_URL)
session = sessionmaker(engine)
