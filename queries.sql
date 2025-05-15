SELECT * FROM dataset



-- 1. Number of house 
SELECT COUNT(*) AS num_house
FROM dataset 

-- 2. Average price 
SELECT CAST(AVG(price) AS DECIMAL(10,2)) AS avg_price
FROM dataset

-- 3. Number of district 
SELECT COUNT (DISTINCT district ) AS district_num
FROM dataset


-- SECTION 2: DETAIL QUERIES

-- 1. The distribution of district and price
SELECT TOP 5 district,  AVG(price) AS avg_price_of_district
FROM dataset
GROUP BY district
ORDER BY avg_price_of_district DESC

-- 2. The correlation of distance and price
SELECT distance_bins, AVG(price) AS avg_price
FROM dataset
GROUP BY distance_bins

-- 3. The correlation of number of bathrooms and price
SELECT number_of_bathrooms, AVG(price) AS avg_price
FROM dataset
GROUP BY number_of_bathrooms
ORDER BY avg_price DESC

-- 4. The correlation of number of bedrooms and price
SELECT number_of_bedrooms,  AVG(price) AS avg_price
FROM dataset
GROUP BY number_of_bedrooms
ORDER BY avg_price DESC

-- 5. The correlation of apartment_type and avg price
SELECT apartment_type, AVG(price) AS avg_price
FROM dataset
GROUP BY apartment_type

-- 6. The correlation of ownership status and avg price
SELECT ownership_status, AVG(price) AS avg_price
FROM dataset
GROUP BY ownership_status

-- 7. The correlation of corner apartment and avg price
SELECT corner_apartment, AVG(price) AS avg_price
FROM dataset
GROUP BY corner_apartment

-- 8. The correlation of views and avg price
SELECT "view", AVG(price) AS avg_price
FROM dataset 
GROUP BY "view"

-- 9. The correlation of interior status and avg price
SELECT interior_status, AVG(price) AS avg_price
FROM dataset
GROUP BY interior_status