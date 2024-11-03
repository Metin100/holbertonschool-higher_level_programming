#!/usr/bin/python3
"""
Module
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    change_state = session.query(State).filter_by(id=2).one_or_none()
    change_state.name = "New Mexico"
    session.commit()

    if session:
        session.close()
