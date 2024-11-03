# 7-model_state_fetch_all.py
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Check that the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Get the command line arguments
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create the engine
    engine = create_engine(f'mysql+mysqldb://{mysql_user}:{mysql_password}@localhost/{database_name}', pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects sorted by states.id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
