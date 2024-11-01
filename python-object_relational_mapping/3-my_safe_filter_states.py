#!/usr/bin/python3
"""
Connecting to database and listing it
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
    )
    mycursor = db.cursor()
    try:
        mycursor.execute("SELECT * FROM states")
    except MySQLdb.Error as e:
        print(e)
    [print(state) for state in mycursor.fetchall() if state[1] == argv[4]]
    mycursor.close()
    db.close()
