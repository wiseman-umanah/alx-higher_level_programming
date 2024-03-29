#!/usr/bin/python3
"""a script that lists all State objects
from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}"
                           .format(user, pwd, 3306, dbname), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).order_by(asc(State.id)).all()
    for i in data:
        print("{}: {}".format(i.id, i.name))

    session.close()
