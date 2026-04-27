
from db_connection import get_connection
from datetime import datetime


def get_stats_per_property():
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
    cursor.close()
    conn.close()
    return rows


def print_stats_per_property():
    rows = get_stats_per_property()
    print("--- Statistics per property ---")
    # Left-align 10 spaces (included Property, min....)
    print(f"{'Property':<10} {'MIN':<10} {'MAX':<10} {'AVG':<10}")
    for row in rows:
        property_code, min_val, max_val, avg_val = row
        print(f"{property_code:<10} {min_val:<10.2f} {max_val:<10.2f} {avg_val:<10.2f}")


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
    cursor.close()
    conn.close()
    return row


def print_min_value():
    row = get_min_value()
    if row:
        value, id_, code, name, location = row
        print(
            f"MIN value: {value} | id: {id_} | code: {code} | name: {name} | location: {location}")


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
    cursor.close()
    conn.close()
    return row


def print_max_value():
    row = get_max_value()
    if row:
        value, id_, code, name, location = row
        print(
            f"MAX value: {value} | id: {id_} | code: {code} | name: {name} | location: {location}")


def get_average_value():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT AVG(value)
            FROM measurements
        """)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row


def print_average_value():
    row = get_average_value()
    print(f"AVG value: {row})")


def get_total_consumption_per_property():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            SELECT 
                p.name,
                SUM(e.value) AS total_kwh
            FROM electricity e
            JOIN properties p ON p.id = e.property
            GROUP BY p.name;
        """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def print_total_consumption_per_property():
    rows = get_total_consumption_per_property()
    print("--- Total Consumption per Property ---")
    print(f"{'Property':<20} {'Total':<20}")
    for row in rows:
        property, total = row
        print(f"{property:<20} {total:<20.2f}")


def get_most_energy_intensive_property():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            SELECT 
                p.name,
                SUM(e.value) AS total_kwh
            FROM electricity e
            JOIN properties p ON p.id = e.property
            GROUP BY p.name
            ORDER BY total_kwh DESC
            LIMIT 1;
        """)
    print("--- Most Energy-Intensive Property ---")
    print(f"{'Name':<20} {'Total kwh':<20}")
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row


def print_most_energy_intensive_property():
    row = get_most_energy_intensive_property()
    if row:
        name, total_kwh = row
        print(f"{name:<20} {total_kwh:<20.2f}")


def get_average_daily_consumption():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            SELECT 
                p.name,
                AVG(e.value) AS avg_kwh
            FROM electricity e
            JOIN properties p ON p.id = e.property
            GROUP BY p.name;
        """)
    print("--- Average Daily Consumption ---")
    print(f"{'Name':<20} {'Average kwh':<20}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def print_average_daily_consumption():
    rows = get_average_daily_consumption()
    for row in rows:
        name, avg_kwh = row
        print(f"{name:<20} {avg_kwh:<20.2f}")


def get_full_report():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            SELECT 
                p.name,
                SUM(e.value) AS total,
                AVG(e.value) AS avg_daily,
                MAX(e.value) AS max_daily
            FROM electricity e
            JOIN properties p ON p.id = e.property
            GROUP BY p.name;
        """)
    print("--- Full Report ---")
    print(f"{'Name':<20} {'Total':<20} {'Avg daily':<20} {'Max daily':<20}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def print_full_report():
    rows = get_full_report()
    for row in rows:
        name, total, avg_daily, max_daily = row
        print(f"{name:<20} {total:<20.2f} {avg_daily:<20.2f} {max_daily:<20.2f}")


def detect_anomalies():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            SELECT 
                p.name,
                e.timestamp,
                e.value
            FROM electricity e
            JOIN properties p ON p.id = e.property
            WHERE e.value > (
                SELECT 2 * AVG(e2.value)
                FROM electricity e2
                WHERE e2.property = e.property
            );
        """)
    print("--- Full Report ---")
    print(f"{'Name':<20} {'Timestamp':<30} {'Value':<20}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def print_detect_anomalies():
    rows = detect_anomalies()
    for row in rows:
        name, timestamp, value = row
        print(f"{name:<20} {timestamp.strftime("%Y-%m-%d %H:%M:%S"):<30} {value:< 20}")


def get_highest_daily_consumption():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            SELECT 
                p.name,
                e.timestamp AS day,
                e.value
            FROM electricity e
            JOIN properties p ON p.id = e.property
            WHERE (e.property, e.value) IN (
                SELECT 
                    property,
                    MAX(value)
                FROM electricity
                GROUP BY property
            );
        """)
    print("--- Highest Daily Consumption ---")
    print(f"{'Name':<20} {'Day':<20} {'Value':<20}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()


def print_highest_daily_consumption():
    rows = get_highest_daily_consumption()
    for row in rows:
        name, timestamp, value = row
        print(f"{name:<20} {timestamp.strftime("%Y-%m-%d"):<20} {value:< 20}")


def get_daily_ranking():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            SELECT 
                e.timestamp,
                p.name,
                e.value,
                RANK() OVER (
                    PARTITION BY e.timestamp
                    ORDER BY e.value DESC
                ) AS rank_pos
            FROM electricity e
            JOIN properties p ON p.id = e.property
            ORDER BY e.timestamp, rank_pos;
        """)
    print("--- Daily Ranking ---")
    print(f"{'Timestamp':<20} {'Name':<20} {'Value':<20} {'Rank Position':<20}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def print_daily_ranking():
    rows = get_daily_ranking()
    for row in rows:
        timestamp, name, value, rank_pos = row
        print(
            f"{timestamp.strftime("%Y-%m-%d"):<20} {name:<20}  {value:< 20} {rank_pos:< 20}")


def get_3day_moving_avg():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
            SELECT 
                p.name,
                e.timestamp,
                AVG(e.value) OVER (
                    PARTITION BY e.property
                    ORDER BY e.timestamp
                    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
                ) AS avg_3_day
            FROM electricity e
            JOIN properties p ON p.id = e.property
            ORDER BY p.name, e.timestamp;
        """)
    print("--- 3-Day Moving Average ---")
    print(f"{'Name':<20} {'Timestamp':<20} {'Average 3 day':<20}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def print_3day_moving_avg():
    rows = get_3day_moving_avg()
    for row in rows:
        name, timestamp, avg_3_day = row
        print(
            f"{name:<20}  {timestamp.strftime("%Y-%m-%d"):<20} {avg_3_day:< 20}")


# print("Choose statistic:")
# print("1. MIN")
# print("2. MAX")
# print("3. AVG")
# print("4. Stats Per Property")
# print("5. Total Consumption per Property")
# print("6. Most Energy-Intensive Property")
# print("7. Average Daily Consumption")
# print("8. Full Report")
# print("9. Detect Anomalies")
# print("10. Highest Daily Consumption")
# print("11. Daily Ranking")
# print("12. 3-Day Moving Average")


# print("0. Exit")


# while True:
#     choice = input("Your choice: ")

#     if choice == "1":
#         get_min_value()
#     # -----------------------------
#     # MAX
#     # -----------------------------
#     elif choice == "2":
#         # sorts measurements table based on the value column in descending order(largest to smallest) and get the first row
#         get_max_value()

#     # -----------------------------
#     # AVG
#     # -----------------------------
#     elif choice == "3":
#         get_average_value()
#     elif choice == "4":
#         stats_per_property()
#     elif choice == "5":
#         print_total_consumption_per_roperty()
#     elif choice == "6":
#         get_most_energy_intensive_property()
#     elif choice == "7":
#         get_average_daily_consumption()
#     elif choice == "8":
#         get_full_report()
#     elif choice == "9":
#         detect_anomalies()
#     elif choice == "10":
#         get_highest_daily_consumption()
#     elif choice == "11":
#         get_daily_ranking()
#     elif choice == "12":
#         get_3day_moving_avg()

#     elif choice == "0":
#         break
#     else:
#         print("❌ Invalid choice")
