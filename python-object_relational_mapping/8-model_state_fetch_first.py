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

    # Create a configured Session class
    Session = sessionmaker(bind=db_engine)

    # Create a instance of Session class
    session = Session()

    # Query state table and print 1st result
    state = session.query(State).order_by(State.id).first()

    if state is not None:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')

    # Close session
    session.close()
