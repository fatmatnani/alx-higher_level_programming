#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
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

    # Connect to the MySQL server
    db = MySQLdb.connect(user=user, passwd=password, db=database)

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the query to retrieve all states, ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the result set
    rows = cur.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
