CREATE TABLE IF NOT EXISTS electricity_prices (
    country VARCHAR(100) NOT NULL,
    iso3_code VARCHAR(3) NOT NULL,
    date DATE NOT NULL,
    price DECIMAL(10,2) NOT NULL,

    PRIMARY KEY (iso3_code, date),
    INDEX(date)
);