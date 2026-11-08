
from sqlalchemy import create_engine 
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base


DATABASE_URL = "postgresql://username:password@localhost:5432/database_name"

engine = create_engine(DATABASE_URL, pool_pre_ping=True) 
# ei engine kaj hocca data base er shathay connetion toire kora. 
# data base er connection asay but  daed hoia gasay taholay notun kora connection make korbay  
# data base er connection asay taholay r connection korar dorkar nai

SessionLocal = sessionmaker(autocommit=False,autoflush=True,bind=engine)
#autoflush er kaj ki 
# autocommit er kaj ki jantay hobay


def get_db():
    db= SessionLocal()
    try:
        yield db

    finally:
        db.close()


def create_tables():
    Base.metadata.create_all(bind=engine)