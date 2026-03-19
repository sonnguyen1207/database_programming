# Module Imports
import json
from db_connection import get_connection
import random


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
cursor.execute("SELECT id FROM properties")
property_ids = [row[0] for row in cursor.fetchall()]

for data in d:
    query = "INSERT INTO electricity(property,timestamp,value) VALUES (%s, %s, %s)"
    values = (random.choice(property_ids), data['timestamp'], data['value'])
    cursor.execute(query, values)

conn.commit()

# Clean up cursor resource
cursor.close()
print("✅ Data inserted from JSON")
