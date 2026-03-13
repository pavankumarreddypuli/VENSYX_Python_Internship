#This file loads all datasets once so every insight file can reuse them.

import pandas as pd

def load_datasets():

    properties = pd.read_csv("data/properties.csv")
    customers = pd.read_csv("data/customers.csv")
    search = pd.read_csv("data/customer_search_history.csv")
    wishlist = pd.read_csv("data/customer_wishlist.csv")
    visits = pd.read_csv("data/customer_visit_history.csv")
    contact = pd.read_csv("data/customer_contact_owner.csv")

    return properties, customers, search, wishlist, visits, contact

