#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cus = db.cursor()
    cus.execute("SELECT * FROM states ORDER BY id ASC")
    [print(state) for state in cus.fetchall()]
    cus.close()
    db.close()
