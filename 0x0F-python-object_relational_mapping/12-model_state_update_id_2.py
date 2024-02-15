#!/usr/bin/python3
"""a script that changes the name of a
State object from the database hbtn_0e_6_usa"""
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

    data = session.query(State).filter(State.id == 2).first()
    data.name = "New Mexico"

    session.commit()

    session.close()
