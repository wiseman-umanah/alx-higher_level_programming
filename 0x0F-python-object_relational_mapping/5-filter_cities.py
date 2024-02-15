#!/usr/bin/python3
"""a script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa"""
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
    cities = []

    con = MySQLdb.connect(host=host, passwd=pd, db=dbName,
                          user=user, port=port)

    cur = con.cursor()
    cur.execute(f"SELECT cities.name FROM cities\
                JOIN states\
                WHERE cities.state_id = states.id\
                AND states.name = 'Texas'\
                ORDER BY cities.id ASC;")

    result = cur.fetchall()
    for i in result:
        cities.append(i[0])

    print(", ".join(cities))

    cur.close()
    con.close()
