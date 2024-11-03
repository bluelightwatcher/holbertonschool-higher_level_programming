#!/usr/bin/python3

"""This module queries data from database.

Uses MySQLdb to write sql query.
Uses the sys module to gather data from the CLI.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """ Using sys module"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """Database settings"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    """implementing cursor"""
    cursor = db.cursor()

    """ Execute SQL query in SQL"""
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    """ retrieving all rows with cursor"""
    rows = cursor.fetchall()

    """printing the row""" 
    for row in rows:
        print(row)

    """ closing cursor and database"""
    cursor.close()
    db.close()
