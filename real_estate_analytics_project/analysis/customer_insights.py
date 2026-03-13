from load_data import load_datasets

properties, customers, search, wishlist, visits, contact = load_datasets()

def most_active_customers():

    active = search["customer_id"].value_counts().head(10)
    print("Top Active Customers")
    print(active)