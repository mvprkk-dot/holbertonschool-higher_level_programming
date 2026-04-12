#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a."""
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

    # Adında 'a' olan bütün ştatlar tapılır və silinir
    states_to_delete = session.query(State).filter(State.name.contains('a'))\
                                          .all()
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()
