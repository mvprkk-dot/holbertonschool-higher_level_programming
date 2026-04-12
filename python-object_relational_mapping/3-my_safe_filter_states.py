#!/usr/bin/python3
"""
Lists all values in the states table of hbtn_0e_0_usa
where name matches the argument and is safe from MySQL injections.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Verilənlər bazasına qoşulma
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    # Təhlükəsiz sorğu: arqumenti parametr kimi ötürürük
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
