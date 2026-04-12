#!/usr/bin/python3
"""Prints all City objects from the database based on State name."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    u, p, d, s_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(u, p, d)
    engine = create_engine(uri, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(City).join(State).filter(State.name == s_name).order_by(City.id).all()

    for city in res:
        print("{}: ({}) {}".format(s_name, city.id, city.name))

    session.close()
