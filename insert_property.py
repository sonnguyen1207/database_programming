from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()


def list_properties():
    cursor.execute("SELECT * FROM properties")
    for row in cursor.fetchall():
        print(row)


def add_property(code, name, location):
    cursor.execute(
        "INSERT INTO properties (code, name, location) VALUES (?, ?, ?)",
        (code, name, location)
    )
    conn.commit()
    print("✅ Added")


def delete_property(property_id):
    cursor.execute("DELETE FROM properties WHERE id = ?", (property_id,))
    conn.commit()
    print("🗑 Deleted")


# --- MENU ---
while True:
    print("\n1. List\n2. Add\n3. Delete\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        list_properties()

    elif choice == "2":
        code = input("Code: ")
        name = input("Name: ")
        location = input("Location: ")
        add_property(code, name, location)

    elif choice == "3":
        pid = int(input("ID to delete: "))
        delete_property(pid)

    elif choice == "4":
        break

conn.close()
