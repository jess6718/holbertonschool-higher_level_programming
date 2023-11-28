#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    # Query database for all state and city instance via joining tables
    result = session.query(City, State).join(State)

    for city, state in result:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close session
    session.close()
