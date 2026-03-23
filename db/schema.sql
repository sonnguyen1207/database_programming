
-- 1. properties
CREATE TABLE IF NOT EXISTS properties (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    code VARCHAR(100),
    name VARCHAR(200),
    location VARCHAR(200)
);


-- 2. electricity

CREATE TABLE IF NOT EXISTS electricity (
    id INT AUTO_INCREMENT PRIMARY KEY,
    property BIGINT,
    timestamp DATETIME,
    value INT,
    FOREIGN KEY (property) REFERENCES properties(id)
);



-- # 3. measurements


CREATE TABLE IF NOT EXISTS measurements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    property_code VARCHAR(255),
    value FLOAT(10,4),
    time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- # 4. DATA

CREATE TABLE IF NOT EXISTS DATA (
    id TINYINT,
    property_id TINYINT,
    timestamp VARCHAR(255),
    reportingGroup VARCHAR(255),
    value VARCHAR(255),
    unit VARCHAR(255)
);
