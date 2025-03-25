import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Style and color palette
plt.style.use('seaborn-v0_8-pastel')
sns.set_palette("deep")

# Connection
conn = psycopg2.connect("dbname=bia_sales user=postgres host=localhost port=5432")

# 1. Best Selling Products
def plot_best_selling_products(conn):
    query = """
    SELECT product_name, SUM(quantity) AS total_sold 
    FROM galaxy.sales 
    JOIN galaxy.products ON sales.product_id = products.product_id 
    GROUP BY product_name 
    ORDER BY total_sold DESC
    """
    df = pd.read_sql(query, conn)
    
    plt.figure(figsize=(14, 7))
    ax = sns.barplot(x="product_name", y="total_sold", data=df, 
                     edgecolor='black', linewidth=1)
    plt.title("Best Selling Products", fontsize=16, fontweight='bold')
    plt.xlabel("Product Name", fontsize=12)
    plt.ylabel("Total Quantity Sold", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add value labels on top of each bar
    for i, v in enumerate(df['total_sold']):
        ax.text(i, v, str(int(v)), ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.show()

# 2. Sales per Store
def plot_sales_per_store(conn):
    query = """
    SELECT 
        st.store_address, 
        SUM(p.price * s.quantity) as total_amount 
    FROM galaxy.sales s 
    JOIN galaxy.stores st ON s.store_id = st.store_id 
    JOIN galaxy.products p ON s.product_id = p.product_id 
    GROUP BY st.store_address 
    ORDER BY total_amount DESC
    """
    df = pd.read_sql(query, conn)
    
    plt.figure(figsize=(14, 7))
    ax = sns.barplot(x="store_address", y="total_amount", data=df, 
                     edgecolor='black', linewidth=1)
    plt.title("Total Sales by Store Location", fontsize=16, fontweight='bold')
    plt.xlabel("Store Address", fontsize=12)
    plt.ylabel("Total Sales Amount (Ksh)", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # labels on top of each bar
    for i, v in enumerate(df['total_amount']):
        ax.text(i, v, f'Ksh {v:,.0f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.show()

# 3. Total Revenue by Product
def plot_revenue_by_product(conn):
    query = """
    SELECT
        p.product_name,
        SUM(s.quantity * p.price) AS total_revenue
    FROM galaxy.sales s
    JOIN galaxy.products p ON s.product_id = p.product_id
    GROUP BY p.product_name
    ORDER BY total_revenue DESC
    """
    df = pd.read_sql(query, conn)
    
    plt.figure(figsize=(14, 7))
    ax = sns.barplot(x="product_name", y="total_revenue", data=df, 
                     edgecolor='black', linewidth=1)
    plt.title("Total Revenue by Product", fontsize=16, fontweight='bold')
    plt.xlabel("Product Name", fontsize=12)
    plt.ylabel("Total Revenue (Ksh)", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # labels on top of each bar
    for i, v in enumerate(df['total_revenue']):
        ax.text(i, v, f'Ksh {v:,.0f}', ha='left', va='bottom', fontweight='bold', rotation=45)
        
    
    plt.tight_layout()
    plt.show()

# 4. Best Selling Product in Each Store
def plot_best_selling_product_by_store(conn):
    query = """
    WITH store_sales AS (
        SELECT
            st.store_address,
            p.product_name,
            SUM(s.quantity) AS total_quantity
        FROM galaxy.sales s
        JOIN galaxy.products p ON s.product_id = p.product_id
        JOIN galaxy.stores st ON s.store_id = st.store_id
        GROUP BY st.store_address, p.product_name
    ), ranked_sales AS (
        SELECT *,
               RANK() OVER (PARTITION BY store_address ORDER BY total_quantity DESC) AS rank
        FROM store_sales
    )
    SELECT
        store_address,
        product_name,
        total_quantity
    FROM ranked_sales
    WHERE rank = 1
    ORDER BY total_quantity DESC
    """
    df = pd.read_sql(query, conn)
    
    plt.figure(figsize=(14, 7))
    ax = sns.barplot(x="store_address", y="total_quantity", hue="product_name", data=df, 
                     edgecolor='black', linewidth=1)
    plt.title("Best Selling Product in Each Store", fontsize=16, fontweight='bold')
    plt.xlabel("Store Address", fontsize=12)
    plt.ylabel("Total Quantity Sold", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.legend(title="Product Name", bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

# 5. Total Sales Revenue per Supplier
def plot_revenue_by_supplier(conn):
    query = """
    SELECT
        sup.supplier_name,
        SUM(supplies.quantity * p.price) as total_worth
    FROM galaxy.supplies supplies
    JOIN galaxy.suppliers sup ON supplies.supplier_id = sup.supplier_id
    JOIN galaxy.products p ON supplies.product_id = p.product_id
    GROUP BY sup.supplier_name
    ORDER BY total_worth DESC
    """
    df = pd.read_sql(query, conn)
    
    plt.figure(figsize=(14, 7))
    ax = sns.barplot(x="supplier_name", y="total_worth", data=df, 
                     edgecolor='black', linewidth=1)
    plt.title("Total Revenue from Each Supplier", fontsize=16, fontweight='bold')
    plt.xlabel("Supplier Name", fontsize=12)
    plt.ylabel("Total Revenue (Ksh)", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # labels on top of each bar
    for i, v in enumerate(df['total_worth']):
        ax.text(i, v, f'Ksh {v:,.0f}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.show()

# plot_best_selling_products(conn)
# plot_sales_per_store(conn)
plot_revenue_by_product(conn)
# plot_best_selling_product_by_store(conn)
# plot_revenue_by_supplier(conn)

conn.close()