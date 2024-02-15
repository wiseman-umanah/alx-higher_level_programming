#!/usr/bin/python3
"""A script that lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    host = "localhost"
    pd = args[2]
    dbName = args[3]
    port = 3306

    con = MySQLdb.connect(host=host, passwd=pd, db=dbName,
                          user=user, port=port)

    cur = con.cursor()
    cur.execute(f"SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states\
                WHERE states.id = cities.state_id\
                ORDER BY cities.id ASC")

    result = cur.fetchall()
    for i in result:
        print(i)

    cur.close()
    con.close()
