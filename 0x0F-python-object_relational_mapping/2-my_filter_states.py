#!/usr/bin/python3
""" A script that takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    """ Connect to the database with username nd paswd in the localhost on port 3306"""
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cus = db.cursor()
    state_name = argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
    cus.execute(query.format(state_name))
    [print(row) for row in cus.fetchall()]
    cus.close()
    db.close()
