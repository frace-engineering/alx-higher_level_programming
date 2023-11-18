#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cus = db.cursor()

    cus.execute(SELECT * FROM states ORDER BY id ASC)
    
    [print(state) for state in cus.fetchall()]

    cus.close()
    db.close()



