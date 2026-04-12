#!/usr/bin/python3
"""Lists all City objects from the database."""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # E501 xətası (sətir uzunluğu) olmasın deyə qısa dəyişənlər
    u, p, d = sys.argv[1], sys.argv[2], sys.argv[3]
    # Port və localhost-u sətiri qısaltmaq üçün kənara çıxarırıq
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(u, p, d)
    engine = create_engine(db, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Join istifadə edərək tək sətirdə bütün şəhərləri və ştatları gətiririk
    res = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in res:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
