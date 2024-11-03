#!/usr/bin/python3
"""
This script lists all State objects from the database hbtn_0e_6_usa,
sorted by ascending id.

It connects to a MySQL database using SQLAlchemy, retrieves all
entries from the State table, and prints each state's id and name.

Usage:
    python3 script.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The username for the MySQL database.
    mysql_password: The password for the MySQL database.
    database_name: The name of the database to connect to.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == '__main__':
    """
    Main entry point of the script. This section will run only
    if the script is executed directly (not imported as a module).
    """

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """
    Establish a connection to the MySQL database using SQLAlchemy.
    The connection string includes the username, password, and database name.
    The pool_pre_ping option is set to True to ensure the connection
    is valid before using it
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    mysql_username, mysql_password, database_name), pool_pre_ping=True)

    """
    Create a sessionmaker object that will be used to create
    a new Session for interacting with the database.
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Query all State objects from the database,
    ordered by id in ascending order. The result is stored
    in the variable 'states'.
    """
    states = session.query(State).order_by(State.id).all()

    """
    Iterate over the retrieved states and print each state's
    id and name in the format "id: name".
    """
    for state in states:
        print(f"{state.id}: {state.name}")

    """
    Close the session to free up resources and ensure that
    all transactions are completed.
    """
    session.close()
