#!/usr/bin/python3
"""
lists all cities of a state from name of a state as an argument,
using the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    states = cur.fetchall()
    st = list(state[0] for state in states)
    print(*st, sep=", ")
    cur.close()
    db.close()
