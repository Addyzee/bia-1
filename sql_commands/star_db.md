CREATE SCHEMA star;

CREATE TABLE star.sales_type (
sales_type_id VARCHAR(20) PRIMARY KEY,
type_name VARCHAR(50) NOT NULL
);

CREATE TABLE star.product (
product_id VARCHAR(20) PRIMARY KEY,
product_name VARCHAR(50) NOT NULL,
product_type VARCHAR(50) NOT NULL,
price FLOAT NOT NULL
);

CREATE TABLE star.time (
time_id VARCHAR(20) PRIMARY KEY,
action_date INT NOT NULL,
action_weekday INT NOT NULL,
action_month int NOT NULL,
action_year int NOT NULL
);

CREATE TABLE star.store (
store_id VARCHAR(20) PRIMARY KEY,
store_address VARCHAR(50) NOT NULL,
city_name VARCHAR(50) NOT NULL,
region_name VARCHAR(50) NOT NULL,
country_name VARCHAR(50) NOT NULL
);

CREATE TABLE star.employees (
employee_id VARCHAR(20) PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
dob DATE NOT NULL
);

CREATE TABLE star.payment_methods (
payment_method_id VARCHAR(20) PRIMARY KEY,
payment_method_name VARCHAR(50) NOT NULL
);

\copy star.sales_type FROM '/tmp/postgres/star/sales_type.csv' DELIMITER ',' HEADER CSV;

\copy star.product FROM '/tmp/postgres/star/products.csv' DELIMITER ',' HEADER CSV;

\copy star.time FROM '/tmp/postgres/star/dim_time.csv' DELIMITER ',' HEADER CSV;

\copy star.store FROM '/tmp/postgres/star/stores.csv' DELIMITER ',' HEADER CSV;

\copy star.employees FROM '/tmp/postgres/star/employees.csv' DELIMITER ',' HEADER CSV;

\copy star.payment_methods FROM '/tmp/postgres/star/payment_methods.csv' DELIMITER ',' HEADER CSV;

### Create fact table

CREATE TABLE star.sales (
product_id VARCHAR(20) references star.product(product_id),
time_id VARCHAR(20) references star.time(time_id),
store_id VARCHAR(20) references star.store(store_id),
employee_id VARCHAR(20) references star.employees(employee_id),
sales_type_id VARCHAR(20) references star.sales_type(sales_type_id),
payment_method_id VARCHAR(20) references star.payment_methods(payment_method_id),
quantity INT NOT NULL
);


### Copy data to the fact table
\copy star.sales FROM '/tmp/postgres/star/sales.csv' DELIMITER ',' HEADER CSV;



### List of all the tables in the database

\dt star.\*

### Queries

SELECT \* FROM <schema>.<table>;

SELECT \* FROM star.sales where quantity > 10;
