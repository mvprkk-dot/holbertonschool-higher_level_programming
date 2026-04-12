#!/usr/bin/python3
"""Lists all City objects from the database."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Arqumentləri birbaşa götürürük, heç bir sabit parol yazmırıq
    u, p, d = sys.argv[1], sys.argv[2], sys.argv[3]
    uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(u, p, d)
    engine = create_engine(uri, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Bütün sorğunu tək sətirdə yazırıq ki, E127 xətası fiziki olaraq QEYRİ-MÜMKÜN olsun
    res = session.query(City, State).join(State, City.state_id == State.id).order_by(City.id).all()

    for city, state in res:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
