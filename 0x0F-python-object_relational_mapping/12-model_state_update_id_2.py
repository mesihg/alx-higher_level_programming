#!/usr/bin/python3
"""
changes the name of a State where id = 2 to New Mexico
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(
        State
    ).filter(
        State.id == 2
    ).update({
        State.name: 'New Mexico'
    })
    session.commit()
