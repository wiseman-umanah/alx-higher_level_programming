#!/usr/bin/python3
"""a script that lists all City objects
from the database hbtn_0e_101_usa"""
import sys
from sqlalchemy import create_engine, asc
from relationship_state import State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}"
                           .format(user, pwd, 3306, dbname))

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(City, State).filter(
        State.id == City.state_id).order_by(asc(City.id))

    for city, state in data:
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
