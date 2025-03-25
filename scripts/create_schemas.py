import pandas as pd

def turn_to_csv(json_file, csv_file, columns=None):
    df = pd.read_json(json_file)
    if columns:
        df = df[columns]
    df.to_csv(csv_file, index=False)
def star_schema():
    # employees
    turn_to_csv('data/employees.json', 'star/employees.csv')
    # sales_type
    turn_to_csv('data/sales_type.json', 'star/sales_type.csv')
    # stores
    turn_to_csv('data/stores.json', 'star/stores.csv', columns=["store_id", "store_address", "city_name", "region_name", "country_name"])
    # products
    turn_to_csv('data/products.json', 'star/products.csv', columns=['product_id', 'product_name', 'product_type', 'price'])
    # payment_methods
    turn_to_csv('data/payment_methods.json', 'star/payment_methods.csv')

def snowflake_schema():
    # employees
    turn_to_csv('data/employees.json', 'snowflake/employees.csv')
    # sales_type
    turn_to_csv('data/sales_type.json', 'snowflake/sales_type.csv')
    # stores
    turn_to_csv('data/stores.json', 'snowflake/stores.csv', columns=["store_id", "store_address", "city_id"])
    # cities
    turn_to_csv('data/cities.json', 'snowflake/cities.csv', columns=["city_id", "city_name", "region_id"])
    # regions
    turn_to_csv('data/regions.json', 'snowflake/regions.csv', columns=["region_id", "region_name", "country_id"])
    # countries
    turn_to_csv('data/countries.json', 'snowflake/countries.csv')
    # products
    turn_to_csv('data/products.json', 'snowflake/products.csv', columns=['product_id', 'product_name', 'product_type_id', 'price'])
    # product types
    turn_to_csv('data/product_types.json', 'snowflake/product_types.csv')
    # payment_methods
    turn_to_csv('data/payment_methods.json', 'snowflake/payment_methods.csv')
    # time
    turn_to_csv('data/dim_time.json', 'snowflake/time.csv', columns=['time_id', 'action_date', 'action_weekday', 'action_month_id'])
    # month
    turn_to_csv('data/dim_month.json', 'snowflake/dim_month.csv')
    # year
    turn_to_csv('data/dim_year.json', 'snowflake/dim_year.csv')
    
def galaxy_schema():
    turn_to_csv('data/suppliers.json', 'galaxy/suppliers.csv')
    
    
# snowflake_schema()
galaxy_schema()

