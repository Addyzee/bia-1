import pandas as pd
from random import shuffle, randint
from typing import Dict
from Assignment1.scripts.generate import (
    generate_employee_numbers,
    generate_times,
    generate_sales_types_number,
    generate_payment_method_number,
    generate_supplier_numbers,
)

product_distribution = [
    {"product_id": "p_1", "product_name": "Maize flour", "sales": 150, "price": 180},
    {"product_id": "p_2", "product_name": "Wheat flour", "sales": 83, "price": 190},
    {"product_id": "p_3", "product_name": "Sugar", "sales": 100, "price": 160},
    {"product_id": "p_4", "product_name": "Rice", "sales": 100, "price": 250},
    {"product_id": "p_5", "product_name": "Cooking oil", "sales": 90, "price": 350},
    {"product_id": "p_6", "product_name": "Salt", "sales": 60, "price": 40},
    {"product_id": "p_7", "product_name": "Tea leaves", "sales": 70, "price": 120},
    {"product_id": "p_8", "product_name": "Instant coffee", "sales": 10, "price": 400},
    {"product_id": "p_9", "product_name": "Smocha", "sales": 80, "price": 50},
    {"product_id": "p_10", "product_name": "Baking powder", "sales": 10, "price": 100},
    {"product_id": "p_11", "product_name": "Bar soap", "sales": 15, "price": 150},
    {"product_id": "p_12", "product_name": "Washing powder", "sales": 15, "price": 250},
    {"product_id": "p_13", "product_name": "Bathing soap", "sales": 20, "price": 100},
    {"product_id": "p_14", "product_name": "Toothpaste", "sales": 20, "price": 180},
    {"product_id": "p_15", "product_name": "Tissue paper", "sales": 55, "price": 90},
    {"product_id": "p_16", "product_name": "Matchboxes", "sales": 10, "price": 20},
    {"product_id": "p_17", "product_name": "Candles", "sales": 15, "price": 60},
    {
        "product_id": "p_18",
        "product_name": "Milk (long life)",
        "sales": 100,
        "price": 70,
    },
    {"product_id": "p_19", "product_name": "Bread", "sales": 90, "price": 60},
    {"product_id": "p_20", "product_name": "Eggs", "sales": 85, "price": 18},
    {
        "product_id": "p_21",
        "product_name": "Soft drinks (soda)",
        "sales": 45,
        "price": 70,
    },
    {"product_id": "p_22", "product_name": "Bottled water", "sales": 20, "price": 50},
    {"product_id": "p_23", "product_name": "Biscuits", "sales": 10, "price": 100},
    {"product_id": "p_24", "product_name": "Sweets", "sales": 5, "price": 5},
    {"product_id": "p_25", "product_name": "Cooking gas", "sales": 20, "price": 3000},
    {"product_id": "p_26", "product_name": "Charcoal", "sales": 30, "price": 800},
    {"product_id": "p_27", "product_name": "Onions", "sales": 15, "price": 20},
    {"product_id": "p_28", "product_name": "Tomatoes", "sales": 20, "price": 25},
    {"product_id": "p_29", "product_name": "Detergent", "sales": 65, "price": 250},
    {
        "product_id": "p_30",
        "product_name": "Blue Band margarine",
        "sales": 15,
        "price": 120,
    },
]


sales_by_region = {
    "Nairobi Region": 550,  # Largest urban population, high purchasing power
    "Rift Valley": 350,  # Large area, mix of urban and rural consumers
    "Coastal Region": 280,  # High tourism & local demand
    "Western Region": 243,  # High population but lower purchasing power
}

sales_by_city = {
    "Nairobi": 550,  # Largest city, high purchasing power
    "Nakuru": 300,  # Large commercial center in Rift Valley
    "Mombasa": 280,  # Coastal trade hub, significant commercial activity
    "Kisumu": 293,  # Major urban center in Western Kenya
}

sales_by_store = {
    "s_1": 280,  # Nairobi (busy city center location)
    "s_2": 270,  # Nairobi (another high-traffic location)
    "s_3": 160,  # Nakuru (urban commercial hub)
    "s_4": 280,  # Mombasa (coastal trade and tourism)
    "s_5": 293,  # Kisumu (major Western Kenya hub)
    "s_6": 140,  # Nakuru (slightly smaller than store s_3)
}


employees_distribution = generate_employee_numbers()
times_distribution = generate_times()
sales_type_distribution = generate_sales_types_number()
payment_method_distribution = generate_payment_method_number()
dates_distribution = {f"d_{i}": 1 for i in range(len(times_distribution))}
supplier_distribution = generate_supplier_numbers()


def create_column(column: Dict[str, int]):
    if type(column) == dict:
        column = list(
            filter(
                ("").__ne__,
                sum([(f"{k}, " * v).split(", ") for k, v in column.items()], []),
            )
        )
    else:
        raise ValueError("Invalid column type")
    shuffle(column)
    return column


def create_sales_data_frame():
    product_ids = {
        product["product_id"]: product["sales"] for product in product_distribution
    }
    product_ids = create_column(product_ids)
    full_time_list = create_column(dates_distribution)
    full_stores_list = create_column(sales_by_store)
    full_employees_list = create_column(employees_distribution)
    full_sales_type_list = create_column(sales_type_distribution)
    full_pm_list = create_column(payment_method_distribution)

    df = pd.DataFrame(
        {
            "product_id": product_ids,
            "sales_type_id": full_sales_type_list,
            "time_id": full_time_list,
            "store_id": full_stores_list,
            "employee_id": full_employees_list,
            "payment_method_id": full_pm_list,
        }
    )
    # df["price"] = df["product_id"].apply(lambda x: next((p["price"] for p in product_distribution if p["product_id"] == x), 0))
    df["quantity"] = df["product_id"].apply(
        lambda _: next(randint(1, 10) for _ in range(1))
    )
    df = df[
        [
            "product_id",
            "time_id",
            "store_id",
            "employee_id",
            "sales_type_id",
            "payment_method_id",
            "quantity",
        ]
    ]
    df.to_csv("star/sales.csv", index=False)


def create_supplies_dataframe():
    product_ids = {
        product["product_id"]: product["sales"] for product in product_distribution
    }
    product_ids = create_column(product_ids)[:500]
    full_time_list = create_column(dates_distribution)[:500]
    full_employees_list = create_column(employees_distribution)[:500]
    full_supplier_list = create_column(supplier_distribution)[:500]

    df = pd.DataFrame(
        {
            "product_id": product_ids,
            "supplier_id": full_supplier_list,
            "time_id": full_time_list,
            "employee_id": full_employees_list,
        }
    )
    df["quantity"] = df["product_id"].apply(
        lambda _: next(randint(1, 10) for _ in range(1))
    )
    print(df)
    df.to_csv("galaxy/supplies.csv", index=False)


# create_sales_data_frame()
create_supplies_dataframe()
