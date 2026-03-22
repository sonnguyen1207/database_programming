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


def delete_property_by_id(property_id):
    cursor.execute("DELETE FROM properties WHERE id = ?", (property_id,))
    conn.commit()
    print("🗑 Deleted")


def delete_property_by_code(property_code):
    # code is unique
    # need to delete children (electricity) before delete parent (property)
    cursor.execute("SELECT id FROM properties WHERE code = ?",
                   (property_code,))
    # delete child rows
    property = cursor.fetchone()
    if not property:
        print("Property not found")
        return
    property_id = property[0]
    cursor.execute(
        "DELETE FROM electricity WHERE property = ?", (property_id,))
    # delete parent
    cursor.execute("DELETE FROM properties WHERE id = ?", (property_id,))
    conn.commit()
    print("🗑 Deleted")


def delete_property_by_name(property_name):
    # property is may still used in another table(electricity), need to delete children first then parent
    # property name may have more than 1 property, need to delete all of their children before delete them
    # get property id
    cursor.execute("SELECT id FROM properties WHERE name = ?",
                   (property_name,))

    for property in cursor.fetchall():
        if not property:
            print("Property not found")
            return

        property_id = property[0]
        # print(property_id)
        # The mycursor.execute(sql, adr) method expects the second argument to be a sequence(like a list or a tuple), not a single string.
        # delete child rows FIRST
        cursor.execute(
            "DELETE FROM electricity WHERE property = ?", (property_id,))
        # then delete parent
        cursor.execute("DELETE FROM properties WHERE id = ?", (property_id,))

    conn.commit()
    print("🗑 Deleted successfully")


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
        # pid = int(input("ID to delete: "))
        # pname = input("Name to delete: ")
        # delete_property_by_name(pname)
        pcode = input("Code to delete: ")
        delete_property_by_code(pcode)

    elif choice == "4":
        break

conn.close()
