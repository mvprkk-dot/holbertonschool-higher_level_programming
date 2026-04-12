#!/usr/bin/python3
"""Changes the name of a State object from the database."""
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

    # id-si 2 olan ştatın tapılması və adının yenilənməsi
    state_to_update = session.query(State).filter(State.id == 2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
