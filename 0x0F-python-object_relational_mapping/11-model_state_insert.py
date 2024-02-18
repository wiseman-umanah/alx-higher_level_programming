#!/usr/bin/python3
"""
a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}"
                           .format(user, pwd, 3306, dbname), echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    newIns = State(name="Louisana")

    session.add(newIns)

    session.commit()
    print(newIns.id)
