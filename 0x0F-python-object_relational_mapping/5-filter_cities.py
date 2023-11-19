#!/usr/bin/python3
"""
    List all cities from the database hbtn_0e_4_usa
    in ASC order of cities.id
    use execute() only once
    script should be safe from sql injection.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    if len(argv) != 5:
        print("Wrong Usage")
        exit(1)
    """ Connect to the database in localhost on port 3306
        using a login user account.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cus = db.cursor()
    state_name = argv[4]
    """ Create the mysql query satement """
    query = "SELECT cities.name FROM cities LEFT JOIN states\
            ON cities.state_id = states.id WHERE  states.name = %s ORDER BY\
            cities.id ASC"
    try:
        """ Execute the query with try keyword """
        cus.execute(query, (state_name,))
        [print(', '.join(row[0] for row in cus.fetchall()))]
    except MySQLdb.Error as error:
        print("Error {}".format(error))
    finally:
        cus.close()
        db.close()
