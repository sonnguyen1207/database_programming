from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

with open("db/migrations/10-24-23-mon-2026-electricity-add-fk-cascade.sql", "r") as f:
    sql = f.read()

# execute multiple statements
for statement in sql.split(";"):
    statement = statement.strip()
    if statement and not statement.startswith("--"):
        cursor.execute(statement)

conn.commit()
cursor.close()

print("✅ Migration executed")
