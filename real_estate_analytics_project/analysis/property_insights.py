
# Most expensive properties
# Average price by state
# Average house size
# Most common property type

from load_data import load_datasets

properties, customers, search, wishlist, visits, contact = load_datasets()

def average_price_by_state():

    avg_price = properties.groupby("state")["price"].mean()

    print("<-----------Average Property Price by State------------->")
    print(avg_price)