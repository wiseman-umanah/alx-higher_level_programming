#!/usr/bin/python3
"""a script that lists all states with a name
starting with N (upper N) from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    port = 3306
    host = "localhost"
    pd = args[2]
    dbName = args[3]

    con = MySQLdb.connect(host=host, passwd=pd, db=dbName,
                          user=user, port=port)

    cur = con.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name LIKE 'N%'\
                ORDER BY states.id ASC")

    result = cur.fetchall()
    for i in result:
        print(i)

    cur.close()
    con.close()
