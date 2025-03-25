CREATE SCHEMA galaxy;

CREATE TABLE galaxy.countries (
country_id VARCHAR(7) PRIMARY KEY,
country_name VARCHAR(50) NOT NULL
);

CREATE TABLE galaxy.regions (
region_id VARCHAR(7) PRIMARY KEY,
region_name VARCHAR(50) NOT NULL,
country_id VARCHAR(7) NOT NULL
);

CREATE TABLE galaxy.cities (
city_id VARCHAR(7) PRIMARY KEY,
city_name VARCHAR(50) NOT NULL,
region_id VARCHAR(7) NOT NULL

);

CREATE TABLE galaxy.stores (
store_id VARCHAR(20) PRIMARY KEY,
store_address VARCHAR(50) NOT NULL,
city_id VARCHAR(7) references galaxy.cities(city_id)
);

CREATE TABLE galaxy.suppliers (
supplier_id VARCHAR(20) PRIMARY KEY,
supplier_name VARCHAR(50) NOT NULL,
city_id VARCHAR(7) references galaxy.cities(city_id)
);

CREATE TABLE galaxy.sales_type (
sales_type_id VARCHAR(20) PRIMARY KEY,
type_name VARCHAR(50) NOT NULL
);

CREATE TABLE galaxy.employees (
employee_id VARCHAR(20) PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
dob DATE NOT NULL
);

CREATE TABLE galaxy.payment_methods (
payment_method_id VARCHAR(20) PRIMARY KEY,
payment_method_name VARCHAR(50) NOT NULL
);

CREATE TABLE galaxy.product_types (
product_type_id VARCHAR(20) PRIMARY KEY,
product_type_name VARCHAR(50) NOT NULL
);

CREATE TABLE galaxy.products (
product_id VARCHAR(20) PRIMARY KEY,
product_name VARCHAR(50) NOT NULL,
product_type_id VARCHAR(20) references galaxy.product_types(product_type_id),
price FLOAT NOT NULL
);

CREATE TABLE galaxy.years (
year_id int PRIMARY KEY,
year_name int NOT NULL
);

CREATE TABLE galaxy.month (
month_id int PRIMARY KEY,
month_name int NOT NULL,
year_id int NOT NULL references galaxy.years(year_id)

);

CREATE TABLE galaxy.time (
time_id VARCHAR(20) PRIMARY KEY,
action_date INT NOT NULL,
action_weekday INT NOT NULL,
month_id int references galaxy.month(month_id)
);

### Copy data
\copy galaxy.countries FROM '/tmp/postgres/snowflake/countries.csv' DELIMITER ',' HEADER CSV;
\copy galaxy.regions FROM '/tmp/postgres/snowflake/regions.csv' DELIMITER ',' HEADER CSV;

\copy galaxy.cities FROM '/tmp/postgres/snowflake/cities.csv' DELIMITER ',' HEADER CSV;

\copy galaxy.stores FROM '/tmp/postgres/snowflake/stores.csv' DELIMITER ',' HEADER CSV;

\copy galaxy.years FROM '/tmp/postgres/snowflake/dim_year.csv' DELIMITER ',' HEADER CSV;

\copy galaxy.month FROM '/tmp/postgres/snowflake/dim_month.csv' DELIMITER ',' HEADER CSV;

\copy galaxy.time FROM '/tmp/postgres/snowflake/time.csv' DELIMITER ',' HEADER CSV;


\copy galaxy.sales_type FROM '/tmp/postgres/snowflake/sales_type.csv' DELIMITER ',' HEADER CSV;

\copy galaxy.employees FROM '/tmp/postgres/snowflake/employees.csv' DELIMITER ',' HEADER CSV;
\copy galaxy.payment_methods FROM '/tmp/postgres/snowflake/payment_methods.csv' DELIMITER ',' HEADER CSV;
\copy galaxy.product_types FROM '/tmp/postgres/snowflake/product_types.csv' DELIMITER ',' HEADER CSV;
\copy galaxy.products FROM '/tmp/postgres/snowflake/products.csv' DELIMITER ',' HEADER CSV;
\copy galaxy.suppliers FROM '/tmp/postgres/galaxy/suppliers.csv' DELIMITER ',' HEADER CSV;

# fact tables
CREATE TABLE galaxy.sales (
product_id VARCHAR(20) references galaxy.products(product_id),
time_id VARCHAR(20) references galaxy.time(time_id),
store_id VARCHAR(20) references galaxy.stores(store_id),
employee_id VARCHAR(20) references galaxy.employees(employee_id),
sales_type_id VARCHAR(20) references galaxy.sales_type(sales_type_id),
payment_method_id VARCHAR(20) references galaxy.payment_methods(payment_method_id),
quantity INT NOT NULL
);

CREATE TABLE galaxy.supplies (
product_id VARCHAR(20) references galaxy.products(product_id),
supplier_id VARCHAR(20) references galaxy.suppliers(supplier_id),
time_id VARCHAR(20) references galaxy.time(time_id),
employee_id VARCHAR(20) references galaxy.employees(employee_id),
quantity INT NOT NULL
);

### Copy data to fact tables
\copy galaxy.sales FROM '/tmp/postgres/snowflake/sales.csv' DELIMITER ',' HEADER CSV;
\copy galaxy.supplies FROM '/tmp/postgres/galaxy/supplies.csv' DELIMITER ',' HEADER CSV;


