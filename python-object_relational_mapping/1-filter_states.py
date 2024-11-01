#!/usr/bin/python3
"""
Connecting to database and listing words which start with uppercase N.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    mycursor = db.cursor()

    try:
        mycursor.execute("SELECT * FROM states ORDER BY id")
        rows = mycursor.fetchall()
    except MySQLdb.Error as e:
        print(e)

    for row in rows:
        if row[1][0] == 'N':
            print(row)
