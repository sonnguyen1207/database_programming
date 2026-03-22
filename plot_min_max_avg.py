import matplotlib.pyplot as plt
from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SELECT MIN(value), MAX(value), AVG(value) FROM measurements")
row = cursor.fetchone()

labels = ["MIN", "MAX", "AVG"]
values = [row[0], row[1], row[2]]

plt.bar(labels, values)
plt.title("Statistics")
plt.show()
