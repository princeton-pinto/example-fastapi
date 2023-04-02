# https://docs.sqlalchemy.org/en/14/orm/session_basics.html
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQL_ALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-addess/hostname:portnumber>/<database_name>'

# SQL_ALCHEMY_DATABASE_URL = 'postgresql://postgres:xxxxxx@localhost:5432/fastapi'

SQL_ALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='xxxxxx', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database connection was SUCCESSFUL')
#         break
#     except Exception as error:
#         print('Connecting to database failed')
#         print('Error:', error)
#         time.sleep(2)