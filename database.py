from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///words.db', echo=True)

Base = declarative_base()
Session = sessionmaker(bind=engine)


class Vocabulary(Base):
    __tablename__ = 'vocabulary'
    v_id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, v_id, name):
        self.v_id = v_id
        self.name = name

    def __repr__(self):
        return f"{self.v_id} {self.name}"


class User(Base):
    __tablename__ = 'user_data'
    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    day_word = Column(Boolean)
    day = Column(String)

    def __init__(self, user_id, username, day_word, day):
        self.user_id = user_id
        self.username = username
        self.day_word = day_word
        self.day = day

    def __repr__(self):
        return f"{self.user_id} {self.username} {self.day_word} {self.day} {self.day}"


Base.metadata.create_all(engine)
