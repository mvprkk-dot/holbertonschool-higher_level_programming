#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    u, p, d = sys.argv[1], sys.argv[2], sys.argv[3]
    # Sətiri tək saxlayırıq ki, heç bir indentation problemi olmasın
    conn = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(u, p, d)
    engine = create_engine(conn, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Bütün sorğunu tək sətirdə yazırıq (E127-nin qarşısını almaq üçün)
    states = session.query(State).filter(State.name.contains('a')).all()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
