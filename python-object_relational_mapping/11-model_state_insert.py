#!/usr/bin/python3
"""Adds the State object 'Louisiana' to the database."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Engine yaradılır
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(sys.argv[1], sys.argv[2],
                                           sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Sessiya yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # Yeni ştat obyektinin yaradılması
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Yeni id-nin çap olunması
    print("{}".format(new_state.id))

    session.close()
