#!/usr/bin/python3
"""
Script that takes an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # MySQL connection parameters
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host=host, port=port, user=user, passwd=password, db=database)

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Prepare the SQL query with user input and execute it
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    # Fetch all the rows from the result set
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
