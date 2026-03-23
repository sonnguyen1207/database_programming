
from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Choose statistic:")
print("1. MIN")
print("2. MAX")
print("3. AVG")
print("4. Exit")


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
        # sorts measurements table based on the value column in ascending order(smallest to largest) and get the first row
        cursor.execute("""
            SELECT value,id ,property_code
            FROM measurements
            ORDER BY value ASC
            LIMIT 1
        """)
        row = cursor.fetchone()
        print(f"MIN value: {row[0]} id: {row[1]} property code: {row[2]}")

    # -----------------------------
    # MAX
    # -----------------------------
    elif choice == "2":
        # sorts measurements table based on the value column in descending order(largest to smallest) and get the first row
        cursor.execute("""
            SELECT value,id ,property_code
            FROM measurements
            ORDER BY value DESC
            LIMIT 1
        """)
        row = cursor.fetchone()
        print(f"MAX value: {row[0]} id: {row[1]} property code: {row[2]}")

    # -----------------------------
    # AVG
    # -----------------------------
    elif choice == "3":
        cursor.execute("""
            SELECT AVG(value)
            FROM measurements
        """)
        row = cursor.fetchone()
        print(f"AVG value: {row})")

    elif choice == "4":
        break
    else:
        print("❌ Invalid choice")

conn.close()
