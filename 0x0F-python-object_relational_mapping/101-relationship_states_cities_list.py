#!/usr/bin/python3
"""a script that lists all State objects,
and corresponding City objects,
contained in the database hbtn_0e_101_usa"""
import sys
from sqlalchemy import create_engine, asc
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}"
                           .format(user, pwd, 3306, dbname))

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State, City).filter(
        State.id == City.state_id).order_by(asc(State.id), asc(City.id))

    state_name = ""

    for state, city in data:
        if state.name != state_name:
            print("{}: {}".format(state.id,  state.name))
            state_name = state.name
        print("\t{}: {}".format(city.id, city.name))

    session.close()
