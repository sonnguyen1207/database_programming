
from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Choose statistic:")
print("1. MIN")
print("2. MAX")
print("3. AVG")
print("4. Exit")

choice = input("Your choice: ")


while True:
    if choice == "1":
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
