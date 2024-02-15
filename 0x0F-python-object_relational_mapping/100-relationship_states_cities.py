#!/usr/bin/python3
"""a script that creates the State “California”
with the City “San Francisco”
from the database hbtn_0e_100_usa"""
import sys
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    dbname = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:{}/{}"
                           .format(user, pwd, 3306, dbname))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    newIns1 = State(name="California")
    newIns2 = City(name="San Francisco", state_id=1)

    session.add_all([newIns1, newIns2])
    session.commit()

    session.close()
