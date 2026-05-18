ALTER TABLE drivers
ADD CONSTRAINT PK_drivers
PRIMARY KEY (driver_id);

ALTER TABLE customers
ADD CONSTRAINT PK_customers
PRIMARY KEY (customer_id);

ALTER TABLE vehicles
ADD CONSTRAINT PK_vehicles
PRIMARY KEY (vehicle_id);

ALTER TABLE zones
ADD CONSTRAINT PK_zones
PRIMARY KEY (zone_id);

ALTER TABLE weather
ADD CONSTRAINT PK_weather
PRIMARY KEY (weather_id);

ALTER TABLE payments
ADD CONSTRAINT PK_payments
PRIMARY KEY (payment_id);