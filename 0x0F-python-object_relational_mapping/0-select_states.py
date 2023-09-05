#!/usr/bin/python3
"""getting all states from sql db
"""

if __name__ == '__main__':
    from sys import argv
    import MySQLdb as mysql

    try:
        db = mysql.connect(host='localhost', port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    except Exception:
        print('Failed to connect to the database')
        exit(0)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC;")

    result_query = cursor.fetchall()

    for row in result_query:
        print(row)

