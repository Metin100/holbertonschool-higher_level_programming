#!/usr/bin/python3
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Retrieve command line arguments
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    
    # Set up the engine and session
    engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@localhost:3306/{db_name}')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query all State objects in ascending order by id
    states = session.query(State).order_by(State.id).all()
    
    # Print each state's id and name
    for state in states:
        print(f"{state.id}: {state.name}")
    
    # Close the session
    session.close()
