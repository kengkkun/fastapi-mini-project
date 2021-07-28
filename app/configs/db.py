import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# db_url = 'aws-us-east-1-portal.17.dblayer.com:11453/compose'
# password = os.environ['COMPOSE_POSTGRESS_PASSWORD']
# connection_string = 'postgres://admin:{}@{}'.format(password, db_url)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR.split('/')[0], ".env"))

connection_string = os.environ["DATABASE_URL"]
Base = declarative_base()
engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)





