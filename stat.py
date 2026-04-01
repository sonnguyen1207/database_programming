
from db_connection import get_connection


def stats_per_property():
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT property_code,
               MIN(value),
               MAX(value),
               AVG(value)
        FROM measurements
        GROUP BY property_code
    """

    cursor.execute(query)
    rows = cursor.fetchall()

    print("--- Statistics per property ---")
    # Left-align 10 spaces (included Property, min....)
    print(f"{'Property':<10} {'MIN':<10} {'MAX':<10} {'AVG':<10}")

    for row in rows:
        property_code, min_val, max_val, avg_val = row
        print(f"{property_code:<10} {min_val:<10.2f} {max_val:<10.2f} {avg_val:<10.2f}")
    cursor.close()
    conn.close()


def get_min_value():
    # from db_connection import get_connection
    conn = get_connection()
    cursor = conn.cursor()

    # sorts measurements table based on the value column in ascending order(smallest to largest) and get the first row
    cursor.execute("""
        SELECT m.value, m.id, p.code, p.name, p.location
        FROM measurements m
        JOIN properties p ON m.property_code = p.code
        ORDER BY m.value ASC
        LIMIT 1
    """)

    row = cursor.fetchone()

    if row:
        value, id_, code, name, location = row
        print(
            f"MIN value: {value} | id: {id_} | code: {code} | name: {name} | location: {location}")

    cursor.close()
    conn.close()


def get_max_value():
    conn = get_connection()
    cursor = conn.cursor()

    # sorts measurements table based on the value column in descending order(largest to smallest) and get the first row
    cursor.execute("""
        SELECT m.value, m.id, p.code, p.name, p.location
        FROM measurements m
        JOIN properties p ON m.property_code = p.code
        ORDER BY m.value DESC
        LIMIT 1
    """)

    row = cursor.fetchone()

    if row:
        value, id_, code, name, location = row
        print(
            f"MAX value: {value} | id: {id_} | code: {code} | name: {name} | location: {location}")

    cursor.close()
    conn.close()


def get_average_value():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT AVG(value)
            FROM measurements
        """)
    row = cursor.fetchone()
    print(f"AVG value: {row})")

    cursor.close()
    conn.close()


print("Choose statistic:")
print("1. MIN")
print("2. MAX")
print("3. AVG")
print("4. Stats Per Property")
print("5. Exit")


while True:
    choice = input("Your choice: ")

    if choice == "1":
        # The "Random Row" Trap: SELECT MIN(value), id, property_code FROM measurements LIMIT 1
        #  nested query (or subquery)
        # cursor.execute("""
        #     SELECT value, id, property_code
        #     FROM measurements
        #     WHERE value = (SELECT MIN(value) FROM measurements);
        # """)
        get_min_value()
    # -----------------------------
    # MAX
    # -----------------------------
    elif choice == "2":
        # sorts measurements table based on the value column in descending order(largest to smallest) and get the first row
        get_max_value()

    # -----------------------------
    # AVG
    # -----------------------------
    elif choice == "3":
        get_average_value()
    elif choice == "4":
        stats_per_property()
    elif choice == "5":
        break
    else:
        print("❌ Invalid choice")
