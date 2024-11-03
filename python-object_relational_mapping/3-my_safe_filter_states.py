#!/usr/bin/python3

"""
This module takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where the name matches the argument,
safely protected from SQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Retrieve command-line arguments:
    username, password, database name, and the state name to search.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    """
    Connect to the MySQL database on localhost at port 3306.
    Use the credentials and database name provided as command-line arguments.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    """
    Create a cursor object to execute SQL queries.
    """
    cursor = db.cursor()

    """
    Execute a parameterized SQL query to avoid SQL injection.
    Use a placeholder (%s) for the state name to securely pass the user input.
    """
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    """
    Fetch all rows in the result set from the executed query.
    """
    rows = cursor.fetchall()

    """
    Print each row retrieved by the query.
    """
    for row in rows:
        print(row)

    """
    Close the cursor and the database connection to free up resources.
    """
    cursor.close()
    db.close()
