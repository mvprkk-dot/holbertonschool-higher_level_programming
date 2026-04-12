#!/usr/bin/python3
"""Prints the State object with the name passed as argument."""
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

    # Ştat adına görə axtarış (SQL injection safe)
    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
