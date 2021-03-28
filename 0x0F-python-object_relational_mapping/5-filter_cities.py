#!/usr/bin/python3
"""Takes in the name state as an argument and lists all cities."""

import MySQLdb
from sys import argv
if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.name\
    FROM cities\
    JOIN states\
    ON state_id=states.id\
    WHERE states.name = %s\
    ORDER BY cities.id ASC", (argv[4],))

    tuples = cursor.fetchall()
    print(", ".join([row[0] for row in tuples]))

    cursor.close()
    db.close()
