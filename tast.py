
from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

print("Choose statistic:")
print("1. MIN")
print("2. MAX")
print("3. AVG")
print("4. SUM")

choice = input("Your choice: ")

# use dictionary to store: key-value choice
functions = {
    "1": "MIN",
    "2": "MAX",
    "3": "AVG",
    "4": "SUM"
}

# if user enter invalid number
if choice not in functions:
    print("❌ Invalid choice")
else:
    # func = functions key(1|2|3|4)
    func = functions[choice]
    # triple quotes let us write strings that span multiple lines
    # Python introduced f-strings (formatted string literals) in version 3.6 to make string formatting and interpolation easier.
    query = f"""
    SELECT 
        property,
        {func}(value)
    FROM electricity
    GROUP BY property
    """

    cursor.execute(query)

    print(f"\nResult ({func}):")
    for row in cursor.fetchall():
        print(f"Property {row[0]} → {func}: {row[1]}")

conn.close()
