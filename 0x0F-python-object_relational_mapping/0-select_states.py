#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

    cus = db.cursor()

    cus.execute("SELECT * FROM states ORDER BY id ASC")
    
    [print(state) for state in cus.fetchall()]

    cus.close()
    db.close()



