#!/usr/bin/python3
""" a script that lists all states from
the database hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    user = args[1]
    pd = args[2]
    dbname = args[3]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=pd, db=dbname)

    cur = db.cursor()
    cur.execute("SELECT * FROM states\
                ORDER BY states.id ASC")
    result = cur.fetchall()
    for i in result:
        print(i)

    cur.close()
    db.close()
