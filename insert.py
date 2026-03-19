# Module Imports
import mariadb
import sys
import json
from db_connection import get_connection


# Read data from file
# open file
f = open('data/091-010-0669-0001.json')
# load json file into d (datalist)
d = json.load(f)
f.close()

# Connect to MariaDB Platform
conn = get_connection()
cursor = conn.cursor()

# delete all dummy data
cursor.execute(
    "DELETE FROM electricity"
)

for data in d:
    query = "INSERT INTO electricity(property,timestamp,value) VALUES (1, %s, %s)"
    values = (data['timestamp'], data['value'])
    cursor.execute(query, values)

conn.commit()

# Clean up cursor resource
cursor.close()

# Close Connection
conn.close()
