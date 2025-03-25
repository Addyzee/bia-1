from datetime import date, timedelta
from random import randint
import pandas as pd

# 1423 is hardcoded as the number of rows in the fact table

ROWS = 1423


def generate_employee_numbers():
    employees = pd.read_json("data/employees.json")
    employees_number = len(employees)
    eq_number = ROWS // employees_number
    if eq_number * employees_number == ROWS:
        employee_numbers = {
            employees.loc[i].employee_id: eq_number for i in range(employees_number)
        }
    else:
        employee_numbers = {
            employees.loc[i].employee_id: eq_number for i in range(employees_number - 1)
        }

        employee_numbers[employees.loc[employees_number - 1].employee_id] = (
            ROWS - eq_number * (employees_number - 1)
        )

    return employee_numbers

def generate_supplier_numbers():
    suppliers = pd.read_json("data/suppliers.json")
    suppliers_number = len(suppliers)
    eq_number = 500 // suppliers_number
    if eq_number * suppliers_number == 500:
        supplier_numbers = {
            suppliers.loc[i].supplier_id: eq_number for i in range(suppliers_number)
        }
    else:
        supplier_numbers = {
            suppliers.loc[i].supplier_id: eq_number for i in range(suppliers_number - 1)
        }

        supplier_numbers[suppliers.loc[suppliers_number - 1].supplier_id] = (
            500 - eq_number * (suppliers_number - 1)
        )

    return supplier_numbers


def generate_sales_types_number():
    cash_transactions = int(0.7 * ROWS)
    return {"s_1": cash_transactions, "s_2": ROWS - cash_transactions}


def generate_payment_method_number():
    cash_transactions = int(0.49 * ROWS)
    mpesa_transactions = int(0.31 * ROWS)
    bank_transactions = int(0.1 * ROWS)
    others = ROWS - (cash_transactions + mpesa_transactions + bank_transactions)

    return {
        "pm_1": cash_transactions,
        "pm_2": mpesa_transactions,
        "pm_3": bank_transactions,
        "pm_4": others,
    }


def generate_times():
    start = date(2024, 7, 1)
    last = date(2024, 7, 30)

    days_no = (last - start).days
    times = []
    record = 0
    for i in range(days_no):
        sales = randint(45, 55)
        sales = ROWS - record if sales + record > ROWS else sales

        if record + sales <= ROWS:
            for _ in range(sales):
                times.append(
                    {
                        "time_id": f"d_{record}",
                        "action_date": (start + timedelta(i)).day,
                        "action_weekday": (start + timedelta(i)).weekday(),
                        "action_month": (start + timedelta(i)).month,
                        "action_month_id": (start + timedelta(i)).month,
                        "action_year": (start + timedelta(i)).year,
                        "action_year_id": (start + timedelta(i)).year,
                    }
                )
                record += 1
        else:
            break
    df = pd.DataFrame(times)
    df.to_csv("data/dim_time.csv", index=False)
    df.to_json("data/dim_time.json", orient="records")
    return times




emp_numbers = generate_employee_numbers()
times = generate_times()
print(sum(emp_numbers.values()))
print(len(times))
