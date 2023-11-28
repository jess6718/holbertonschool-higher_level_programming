#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    # Get user input
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # db_engine is database connector
    db_engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            user, password, db_name),
        pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(db_engine)

    # Create a configured Session class
    Session = sessionmaker(bind=db_engine)

    # Create a instance of Session class
    session = Session()

    # Query database for instance containing "a"
    states = session.query(State).filter(State.name.like('%a%'))
    # Loop deleting instance
    for state in states:
        session.delete(state)

    # Committing the changes to the database
    session.commit()

    # Close session
    session.close()
