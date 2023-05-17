from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///count-on-it.db")
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Counter(Base):
    __tablename__ = "Counter"

    id = Column(Integer, primary_key=True, autoincrement=True)
    Date = Column(String)
    Name = Column(String)
    Count = Column(Integer, default=0)


Base.metadata.create_all(engine)
