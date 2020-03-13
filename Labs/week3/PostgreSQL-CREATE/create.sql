CREATE TABLE cars (
	id_car INTEGER PRIMARY KEY NOT NULL,
	VIN VARCHAR(30) NOT NULL,
	manufacturer VARCHAR(50) NOT NULL,
	model VARCHAR(50) NOT NULL,
	year INTEGER,
	color VARCHAR(30)
);

CREATE TABLE customers (
	id_customer INTEGER PRIMARY KEY NOT NULL,
	customer_id INTEGER NOT NULL,
	name CHAR(30) NOT NULL,
	phone_number VARCHAR(50) NOT NULL,
	email VARCHAR(50),
	id_address INTEGER,
	id_car INTEGER
);

CREATE TABLE address (
	id_address INTEGER PRIMARY KEY NOT NULL,
	address VARCHAR(100),
	city VARCHAR(30),
	state_province VARCHAR(50),
	country VARCHAR(20),
	zip_postal_code INTEGER
);

CREATE TABLE salesperson (
	id_sp INTEGER PRIMARY KEY NOT NULL,
	staff_id VARCHAR(30) NOT NULL,
	name VARCHAR(50) NOT NULL,
	store VARCHAR(50) NOT NULL
);

CREATE TABLE invoices (
	id_invoice INTEGER PRIMARY KEY NOT NULL,
	invoice_number INTEGER,
	date DATE,
	id_car INTEGER,
	id_customer INTEGER,
	id_salesperson INTEGER
);