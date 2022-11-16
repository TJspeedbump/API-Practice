from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


#sqlalchemy_Database_URL = f"postgresql://<username>:<password>@<ip-address/hostname>:<port>/<database_name>"
sqlalchemy_Database_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(sqlalchemy_Database_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# RAW SQL
#while True:
#   try:
#       conn = psycopg2.connect(host="localhost", database="Api", user="postgres", password="Hello13202", cursor_factory=RealDictCursor)
#       cursor = conn.cursor()
#       print("database connect was success")
#        break
#   except Exception as error:
#       print("Failed to connect to database")
#       print("Error: ", error)
#       time.sleep(2)