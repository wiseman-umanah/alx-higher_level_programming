#!/usr/bin/python3
"""a script that prints the State object
with the name passed as argument
from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]
    search = " ".join(sys.argv[4:])

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}"
                           .format(user, pwd, 3306, dbname), echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(State).order_by(asc(State.id)).all()
    dum = 0
    for i in data:
        if search == i.name:
            print(i.id)
            dum = 1
    if dum == 0:
        print("Not found")
    session.close()
