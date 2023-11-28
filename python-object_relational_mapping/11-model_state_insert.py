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
    Base.metadata.create_all(engine)

    # Create a configured Session class
    Session = sessionmaker(bind=db_engine)

    # Create a instance of Session class
    session = Session()

    # Passing Louisiana to create a instance
    add_state = State(name='Louisiana')

    # Adding Louisiana instance to the session
    session.add(add_state)

    # Committing the changes to the database
    session.commit()

    print(add_state.id)

    # Close session
    session.close()
