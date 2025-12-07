from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import declarative_base, sessionmaker


engine: Engine = create_engine("sqlite:///data/data.db")

Base = declarative_base()

Session = sessionmaker(bind=engine)