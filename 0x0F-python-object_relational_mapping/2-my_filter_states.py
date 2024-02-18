#!/usr/bin/python3
"""a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument."""
import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    port = 3306
    host = "localhost"
    pd = args[2]
    dbName = args[3]
    search = args[4]

    con = MySQLdb.connect(host=host, passwd=pd, db=dbName,
                          user=user, port=port)

    cur = con.cursor()
    cur.execute("SELECT * FROM states\
                WHERE name = '{}'\
                ORDER BY states.id ASC".format(search))

    result = cur.fetchall()
    for i in result:
        print(i)

    cur.close()
    con.close()
