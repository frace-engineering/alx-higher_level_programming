#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user="mysql username", passwd="mysql password", db="hbtn_0e_0_usa")

    cus = db.cursor()

    cus.execute(SELECT * FROM states ORDER BY id ASC)
    
    [print(state) for state in cus.fetchall()]

    cus.close()
    db.close()



