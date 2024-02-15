#!/usr/bin/python3
"""a script that prints the first State object
from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}"
                           .format(user, pwd, 3306, dbname), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).filter(State.id == 1).first()
    print("{}: {}".format(data.id, data.name))

    session.close()
