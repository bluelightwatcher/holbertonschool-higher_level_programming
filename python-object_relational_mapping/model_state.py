#!/usr/bin/python3
"""
Module that defines a State class and creates the states table in a MySQL database.
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for declarative class definitions
Base = declarative_base()

class State(Base):
    """
    State class that links to the 'states' table in the MySQL database.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    """
    Main function that connects to the MySQL database and creates the table.
    """
    
    # Create the database engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    
    # Create all tables in the engine (including the states table)
    Base.metadata.create_all(engine)
