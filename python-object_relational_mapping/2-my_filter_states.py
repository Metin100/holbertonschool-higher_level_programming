#!/usr/bin/python3
"""
Connect to a database and list the first row where the name matches the provided argument.
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
        query = """
        SELECT * FROM states WHERE name='{:s}' ORDER BY states.id
        """
        mycursor.execute(query.format(argv[4]))
        rows = mycursor.fetchall()
    except MySQLdb.Error as e:
        print(e)
    
    for row in rows:
        print(row)

    mycursor.close()
    db.close()
