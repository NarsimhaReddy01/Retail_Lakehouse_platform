
from faker import Faker

import pandas as pd
import random
from pathlib import Path

fake = Faker()

BASE = Path("data/raw")
BASE.mkdir(parents=True, exist_ok=True)

# ---------- Customers ----------
customers = []
for cid in range(1, 1001):
    customers.append({
        "customer_id": cid,
        "name": fake.name(),
        "email": fake.email(),
        "city": fake.city(),
        "state": fake.state(),
        "created_date": fake.date_between("-2y", "today")
    })

pd.DataFrame(customers).to_csv(BASE / "customers.csv", index=False)

# ---------- Products ----------
products = []
categories = ["Electronics", "Fashion", "Home", "Sports"]

for pid in range(1, 201):
    products.append({
        "product_id": pid,
        "product_name": fake.word().title(),
        "category": random.choice(categories),
        "price": round(random.uniform(100, 5000), 2)
    })

pd.DataFrame(products).to_csv(BASE / "products.csv", index=False)

# ---------- Orders ----------
orders = []

for oid in range(1, 5001):
    orders.append({
        "order_id": oid,
        "customer_id": random.randint(1, 1000),
        "product_id": random.randint(1, 200),
        "quantity": random.randint(1, 5),
        "order_date": fake.date_between("-1y", "today")
    })

pd.DataFrame(orders).to_csv(BASE / "orders.csv", index=False)

print("Retail datasets generated successfully.")