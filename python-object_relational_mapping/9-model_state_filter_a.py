#!/usr/bin/python3
"""Lists all State objects that contain the letter a."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Engine yaradılır (E501 xətası olmaması üçün formatlanır)
    conn_str = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn_str.format(sys.argv[1], sys.argv[2],
                                           sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Sessiya yaradılır
    Session = sessionmaker(bind=engine)
    session = Session()

    # Adında 'a' hərfi olan ştatlar id üzrə sıralanır
    states_with_a = session.query(State).filter(State.name.contains('a'))\
                                        .order_by(State.id).all()

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()
