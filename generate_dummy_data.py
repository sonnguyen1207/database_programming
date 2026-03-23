import random
from datetime import datetime
from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

# ------------------------
# 1. INSERT properties (MUST FIRST)
# ------------------------
for i in range(1, 11):
    cursor.execute(
        "INSERT INTO properties (code, name, location) VALUES (?, ?, ?)",
        (f"P{i}", f"Property {i}", f"Location {i}")
    )

# ------------------------
# 2. INSERT electricity (FK → properties.id)
# ------------------------
cursor.execute("SELECT id FROM properties")
property_ids = [row[0] for row in cursor.fetchall()]
for _ in range(10):
    cursor.execute(
        "INSERT INTO electricity (property, timestamp, value) VALUES (?, ?, ?)",
        (
            random.choice(property_ids),
            datetime.now(),
            random.randint(100, 500)
        )
    )

# ------------------------
# 3. INSERT measurements
# ------------------------
for i in range(1, 11):
    cursor.execute(
        "INSERT INTO measurements (property_code, value) VALUES (?, ?)",
        (
            f"P{i}",
            round(random.uniform(10, 50), 2)
        )
    )


# ------------------------
# 4. INSERT DATA
# ------------------------
for i in range(1, 11):
    cursor.execute(
        "INSERT INTO DATA (id, property_id, timestamp, reportingGroup, value, unit) VALUES (?, ?, ?, ?, ?, ?)",
        (
            i,
            random.randint(1, 10),
            "2026-01-01",
            "groupA",
            str(random.randint(10, 100)),
            "kWh"
        )
    )

# ------------------------
# SAVE
# ------------------------
# properties
# for i in range(1, 11):
#     cursor.execute(
#         "INSERT INTO properties (code, name, location) VALUES (?, ?, ?)",
#         (f"P{i}", f"Property {i}", f"Location {i}")
#     )

# measurements
# cursor.execute("SELECT id FROM properties")
# property_ids = [row[0] for row in cursor]
# for i in range(10):
#     cursor.execute(
#         "INSERT INTO measurements (property, timestamp, value) VALUES (?, ?, ?)",
#         (
#             random.choice(property_ids),
#             datetime.now(),
#             random.randint(10, 100)
#         )
#     )

# sensor_data
# for i in range(1, 11):
#     cursor.execute(
#         "INSERT INTO sensor_data VALUES (?, ?, ?, ?, ?, ?)",
#         (
#             i,
#             i,
#             "2026-01-01",
#             "groupA",
#             str(20 + i),
#             "C"
#         )
#     )

# log_data
# for i in range(1, 11):
#     cursor.execute(
#         "INSERT INTO log_data (property_code, value) VALUES (?, ?)",
#         (
#             f"P{i}",
#             10.5 + i
#         )
#     )

conn.commit()
conn.close()
print("✅ Dummy data inserted successfully!")
