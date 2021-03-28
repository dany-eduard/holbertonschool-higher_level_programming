#!/usr/bin/python3
"""
Takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv
if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         host="localhost",
                         port=3306)

    cursor = db.cursor()
    upper = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"\
            .format(argv[4])
    cursor.execute(upper)
    list_of_tuples = cursor.fetchall()
    for _tuple in list_of_tuples:
        if _tuple[1] == argv[4]:
            print(_tuple)

    cursor.close()
    db.close()
