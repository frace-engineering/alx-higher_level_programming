#!/usr/bin/python3
"""  This script takes arguments and displays all te values in the states table
    of the hbtn_0e_o_use batabase where name matches the argument.
    Script must be safe from ssql injection.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    if len(argv) != 5:
        print("Wrong usage")
        exit(1)
    """ Connect to the database in localhost on port 3306
        using a login user account.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cus = db.cursor()
    state_name = argv[4]
    """ Create the mysql query satement """
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    try:
        """ Execute the query with try keyword """
        cus.execute(query, (state_name,))
        [print(row) for row in cus.fetchall()]
    except MySQLdb.Error as error:
        print("Error {}".format(error))
    finally:
        cus.close()
        db.close()
