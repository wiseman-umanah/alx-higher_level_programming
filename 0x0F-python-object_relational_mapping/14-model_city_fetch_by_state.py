#!/usr/bin/python3
"""a script 14-model_city_fetch_by_state.py
that prints all City objects
from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}"
                           .format(user, pwd, 3306, dbname), echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(City, State).filter(City.state_id == State.id)
    for i, y in data:
        print("{}: ({}) {}".format(y.name, i.id, i.name))

    session.close()
