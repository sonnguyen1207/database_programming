# Run this file ONLY once to create tables
from db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()

# properties
cursor.execute("""
CREATE TABLE IF NOT EXISTS properties (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(100),
    name VARCHAR(200),
    location VARCHAR(200)
)
""")

# measurements
cursor.execute("""
CREATE TABLE IF NOT EXISTS measurements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    property BIGINT,
    timestamp DATETIME,
    value INT,
    INDEX(property),
    FOREIGN KEY (property) REFERENCES properties(id)
)
""")

# sensor_data
cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id TINYINT,
    property_id TINYINT,
    timestamp VARCHAR(255),
    reportingGroup VARCHAR(255),
    value VARCHAR(255),
    unit VARCHAR(255)
)
""")

# log_data
cursor.execute("""
CREATE TABLE IF NOT EXISTS log_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    property_code VARCHAR(255),
    value FLOAT(10,4),
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")


conn.commit()
conn.close()
