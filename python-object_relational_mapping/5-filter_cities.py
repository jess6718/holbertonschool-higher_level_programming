#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    # mydb is connection object
    mydb = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3])

    # cursorObj is object to execute queries
    cursorObj = mydb.cursor()

    query = "SELECT cities.name FROM cities\
        LEFT JOIN states ON cities.state_id = states.id\
        WHERE BINARY states.name LIKE %s ORDER BY cities.id"
    name = (sys.argv[4],)

    # Execute SQL query to fetch all the states in the database
    cursorObj.execute(query, name)

    # Fetch all the rows and display them
    myresult = cursorObj.fetchall()
    res = ""
    for row in myresult:
        res = res + row[0]+', '
    print(res[:-2])
    # shut cursor and database connection
    cursorObj.close()
    mydb.close()
