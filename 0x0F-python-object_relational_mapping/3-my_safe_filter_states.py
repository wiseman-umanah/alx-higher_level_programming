#!/usr/bin/python3
"""A script that takes in arguments and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
But this time, write one that is safe from MySQL injections!"""
import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    host = "localhost"
    pd = args[2]
    port = 3306
    dbName = args[3]
    search = ' '.join(args[4:])

    con = MySQLdb.connect(host=host, passwd=pd, db=dbName,
                          user=user, port=port)

    cur = con.cursor()
    cur.execute(f"SELECT * FROM states\
                WHERE name = '{search}'\
                ORDER BY states.id ASC")

    result = cur.fetchall()
    for i in result:
        print(i)

    cur.close()
    con.close()
