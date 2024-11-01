#!/usr/bin/python3
"""
Connecting to database and listing it
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

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
        if row[1] == argv[4]:
            print(row)

    mycursor.close()
    db.close()
