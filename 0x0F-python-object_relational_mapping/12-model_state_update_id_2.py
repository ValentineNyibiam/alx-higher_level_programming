#!/usr/bin/python3
"""
    This is a script that changes the name of a State object from
    to the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(f'mysql+mysqldb://{user}:{passwd}@localhost:\
                           3306/{db}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).filter(State.id == 2).first()

    row.name = "New Mexico"

    session.commit()
    session.close()
