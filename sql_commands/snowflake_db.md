CREATE SCHEMA snowflake;

CREATE TABLE snowflake.countries (
country_id VARCHAR(7) PRIMARY KEY,
country_name VARCHAR(50) NOT NULL
);

CREATE TABLE snowflake.regions (
region_id VARCHAR(7) PRIMARY KEY,
region_name VARCHAR(50) NOT NULL,
country_id VARCHAR(7) NOT NULL
);

CREATE TABLE snowflake.cities (
city_id VARCHAR(7) PRIMARY KEY,
city_name VARCHAR(50) NOT NULL,
region_id VARCHAR(7) NOT NULL

);


CREATE TABLE snowflake.stores (
store_id VARCHAR(20) PRIMARY KEY,
store_address VARCHAR(50) NOT NULL,
city_id VARCHAR(7) references snowflake.cities(city_id)
);




CREATE TABLE snowflake.years (
year_id int PRIMARY KEY,
year_name int NOT NULL
);


CREATE TABLE snowflake.month (
month_id int PRIMARY KEY,
month_name int NOT NULL,
year_id int NOT NULL references snowflake.years(year_id)

);


CREATE TABLE snowflake.time (
time_id VARCHAR(20) PRIMARY KEY,
action_date INT NOT NULL,
action_weekday INT NOT NULL,
month_id int references snowflake.month(month_id)
);


CREATE TABLE snowflake.sales_type (
sales_type_id VARCHAR(20) PRIMARY KEY,
type_name VARCHAR(50) NOT NULL
);

CREATE TABLE snowflake.employees (
employee_id VARCHAR(20) PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
dob DATE NOT NULL
);

CREATE TABLE snowflake.payment_methods (
payment_method_id VARCHAR(20) PRIMARY KEY,
payment_method_name VARCHAR(50) NOT NULL
);

CREATE TABLE snowflake.product_types (
product_type_id VARCHAR(20) PRIMARY KEY,
product_type_name VARCHAR(50) NOT NULL
);

CREATE TABLE snowflake.products (
product_id VARCHAR(20) PRIMARY KEY,
product_name VARCHAR(50) NOT NULL,
product_type_id VARCHAR(20) references snowflake.product_types(product_type_id),
price FLOAT NOT NULL
);

### Copy data
\copy snowflake.countries FROM '/tmp/postgres/snowflake/countries.csv' DELIMITER ',' HEADER CSV;
\copy snowflake.regions FROM '/tmp/postgres/snowflake/regions.csv' DELIMITER ',' HEADER CSV;

\copy snowflake.cities FROM '/tmp/postgres/snowflake/cities.csv' DELIMITER ',' HEADER CSV;

\copy snowflake.stores FROM '/tmp/postgres/snowflake/stores.csv' DELIMITER ',' HEADER CSV;

\copy snowflake.years FROM '/tmp/postgres/snowflake/dim_year.csv' DELIMITER ',' HEADER CSV;

\copy snowflake.month FROM '/tmp/postgres/snowflake/dim_month.csv' DELIMITER ',' HEADER CSV;

\copy snowflake.time FROM '/tmp/postgres/snowflake/time.csv' DELIMITER ',' HEADER CSV;


\copy snowflake.sales_type FROM '/tmp/postgres/snowflake/sales_type.csv' DELIMITER ',' HEADER CSV;

\copy snowflake.employees FROM '/tmp/postgres/snowflake/employees.csv' DELIMITER ',' HEADER CSV;
\copy snowflake.payment_methods FROM '/tmp/postgres/snowflake/payment_methods.csv' DELIMITER ',' HEADER CSV;
\copy snowflake.product_types FROM '/tmp/postgres/snowflake/product_types.csv' DELIMITER ',' HEADER CSV;
\copy snowflake.products FROM '/tmp/postgres/snowflake/products.csv' DELIMITER ',' HEADER CSV;



### Create fact table

CREATE TABLE snowflake.sales (
product_id VARCHAR(20) references snowflake.products(product_id),
time_id VARCHAR(20) references snowflake.time(time_id),
store_id VARCHAR(20) references snowflake.stores(store_id),
employee_id VARCHAR(20) references snowflake.employees(employee_id),
sales_type_id VARCHAR(20) references snowflake.sales_type(sales_type_id),
payment_method_id VARCHAR(20) references snowflake.payment_methods(payment_method_id),
quantity INT NOT NULL
);

### Copy data to fact tables
\copy snowflake.sales FROM '/tmp/postgres/snowflake/sales.csv' DELIMITER ',' HEADER CSV;





