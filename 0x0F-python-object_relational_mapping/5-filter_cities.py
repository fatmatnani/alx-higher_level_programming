#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host="localhost", port=3306)
    cursor = db.cursor()
    state_name = sys.argv[4]
    cursor.execute("SELECT cities.name FROM cities \
                    JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC", (state_name,))
    cities = cursor.fetchall()
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))
    cursor.close()
    db.close()
