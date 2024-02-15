#!/usr/bin/python3
"""a script that deletes all State objects
with a name containing the
letter a from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}"
                           .format(user, pwd, 3306, dbname), echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).order_by(asc(State.id)).all()
    for i in data:
        if "a" in i.name:
            session.delete(i)
            session.commit()

    session.close()
