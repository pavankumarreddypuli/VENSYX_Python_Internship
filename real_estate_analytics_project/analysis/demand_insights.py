
# Most searched property types
# Most wishlisted properties
# Most visited properties
# Most contacted properties

from load_data import load_datasets

properties, customers, search, wishlist, visits, contact = load_datasets()

def most_wishlisted_properties():

    top = wishlist["property_id"].value_counts().head(10)

    print("<------------Top Wishlisted Properties------------>")
    print(top)