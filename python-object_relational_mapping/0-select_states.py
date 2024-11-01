#!/usr/bin/python3
"""
Connecting to database and listing it
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = argv[1],
        passwd = argv[2],
        database = argv[3]
    )
    mycursor = db.cursor()
    try:
        mycursor.execute("""SELECT * FROM states ORDER BY id""")
        data = mycursor.fetchall()
    except MySQLdb.Error as e:
        print(e)

    for row in data:
        print(row)
    
    mycursor.close()
    db.close()