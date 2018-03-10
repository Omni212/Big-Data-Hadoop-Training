CREATE EXTERNAL TABLE IF NOT EXISTS Cars(
        Name STRING, 
        Miles_per_Gallon INT,
        Cylinders INT,
        Displacement INT,
        Horsepower INT, 
        Weight_in_lbs INT,
        Acceleration DECIMAL,
        Year DATE,
        Origin CHAR(1))
    COMMENT 'Data about cars from a public database'
    ROW FORMAT DELIMITED
    FIELDS TERMINATED BY ','
    STORED AS TEXTFILE
    location '/user/hive/cars';