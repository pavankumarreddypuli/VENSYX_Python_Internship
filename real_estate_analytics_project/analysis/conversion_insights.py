
# Insights:
# Search → Wishlist → Visit → Contact

from load_data import load_datasets

properties, customers, search, wishlist, visits, contact = load_datasets()

def conversion_funnel():

    print("Search Count:", len(search))
    print("Wishlist Count:", len(wishlist))
    print("Visit Count:", len(visits))
    print("Contact Count:", len(contact))