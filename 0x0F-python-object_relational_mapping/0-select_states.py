#!/usr/bin/python3
"""List all states from the database."""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    """Connect to a MySQL server."""
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)

    """Used to instantiate a MySQL cursor object."""
    cursor = db.cursor()

    """Executes the given database operation (query or command)."""
    sort = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sort)

    """Fetches all rows of a query result set and returns a list of tuples."""
    list_of_tuples = cursor.fetchall()
    for _tuple in list_of_tuples:
        print(_tuple)

    """
    Closes the cursor, resets all results, and ensures that the cursor object
    has no reference to its original connection object.
    """
    cursor.close()
    db.close()
