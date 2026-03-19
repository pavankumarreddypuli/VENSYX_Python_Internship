from load_data import load_datasets
import numpy as np
import pandas as pd

# Load datasets
properties, customers, search, wishlist, visits, contact = load_datasets()


def recommend_properties(customer_id):

    df = properties.copy()

    print(f"\n------------------- SMART RECOMMENDATION SYSTEM ----------------------")
    print(f"Customer ID: {customer_id}")

    #GET USER BEHAVIOR DATA

    user_search = search[search["customer_id"] == customer_id]
    user_wishlist = wishlist[wishlist["customer_id"] == customer_id]
    user_visits = visits[visits["customer_id"] == customer_id]

    interested_props = set(user_search["property_id"]) | \
                       set(user_wishlist["property_id"]) | \
                       set(user_visits["property_id"])

    #IF NO DATA → FALLBACK

    if len(interested_props) == 0:
        print("No user behavior found → Showing general best properties")
        return
    
    #FILTER TO PROPERTIES USER INTERACTED WITH
    user_df = df[df["property_id"].isin(interested_props)]

    #LEARN USER PREFERENCES
    #Average price user prefers
    avg_price = user_df["price"].mean()
    avg_size = user_df["house_size_sqft"].mean()
    preferred_state = user_df["state"].mode()[0]

    print(f"\nLearned Preferences:")
    print(f"→ Preferred Price: {int(avg_price)}")
    print(f"→ Preferred Size: {int(avg_size)}")
    print(f"→ Preferred State: {preferred_state}")

    #SOFT FILTER (NOT STRICT)

    df = df[
        (df["price"].between(0.5 * avg_price, 1.5 * avg_price)) &
        (df["house_size_sqft"].between(0.5 * avg_size, 1.5 * avg_size))
    ]

    if df.empty:
        print("No matching properties found after filtering")
        return

    #NORMALIZATION

    df["price_score"] = (df["price"].max() - df["price"]) / (df["price"].max() - df["price"].min())

    df["size_score"] = (df["house_size_sqft"] - df["house_size_sqft"].min()) / \
                       (df["house_size_sqft"].max() - df["house_size_sqft"].min())
    
    #Lower crime = better
    df["safety_score"] = (df["crime_rate_index"].max() - df["crime_rate_index"]) / \
                         (df["crime_rate_index"].max() - df["crime_rate_index"].min())

    #LOCATION SCORE
    
    '''Why 1/(distance+1)?
    Smaller distance → bigger score'''

    df["location_score"] = (
        0.5 * (1 / (df["metro_distance_km"] + 1)) +
        0.3 * (1 / (df["nearby_schools_km"] + 1)) +
        0.2 * (1 / (df["nearby_hospitals_km"] + 1))
    )

    #SOFT STATE PREFERENCE (NOT HARD FILTER)

    df["state_score"] = (df["state"] == preferred_state).astype(int)

    #DIVERSITY (VERY IMPORTANT)

    # STATE DIVERSITY
    state_counts = df["state"].value_counts().to_dict()
    df["state_diversity"] = df["state"].apply(lambda x: 1 / state_counts[x]).astype(float)

    # PRICE DIVERSITY
    df["price_bucket"] = pd.qcut(df["price"], q=3, labels=["low", "mid", "high"], duplicates="drop")
    price_counts = df["price_bucket"].value_counts().to_dict()
    df["price_diversity"] = df["price_bucket"].apply(lambda x: 1 / price_counts[x]).astype(float)

    # SIZE DIVERSITY
    df["size_bucket"] = pd.qcut(df["house_size_sqft"], q=3, labels=["small", "medium", "large"], duplicates="drop")
    size_counts = df["size_bucket"].value_counts().to_dict()
    df["size_diversity"] = df["size_bucket"].apply(lambda x: 1 / size_counts[x]).astype(float)
    #FINAL HYBRID SCORE

    df["final_score"] = (
    0.25 * df["price_score"] +
    0.20 * df["size_score"] +
    0.25 * df["location_score"] +
    0.20 * df["safety_score"] +
    0.05 * df["state_score"] +
    
    # SMART DIVERSITY
    0.02 * df["state_diversity"] +
    0.015 * df["price_diversity"] +
    0.015 * df["size_diversity"]
)

    #TOP RECOMMENDATIONS

    top = df.sort_values(by="final_score", ascending=False).head(10)

    print("\n---------- SMART RECOMMENDATIONS -----------")
    print(top[[
        "property_id",
        "state",
        "price",
        "house_size_sqft",
        "final_score"
    ]])