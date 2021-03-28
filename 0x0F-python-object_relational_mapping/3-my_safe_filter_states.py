#!/usr/bin/python3
"""
cript that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!
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
    upper = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"
    cursor.execute(upper, (argv[4],))
    list_of_tuples = cursor.fetchall()
    for _tuple in list_of_tuples:
        if _tuple[1] == argv[4]:
            print(_tuple)

    cursor.close()
    db.close()
