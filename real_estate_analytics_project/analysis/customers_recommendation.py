from load_data import load_datasets
import numpy as np
import pandas as pd

# Load datasets
properties, customers, search, wishlist, visits, contact = load_datasets()


def recommend_properties(customer_id):

    df = properties.copy()

    print(f"\n------------------- SMART RECOMMENDATION SYSTEM ----------------------")
    print(f"Customer ID: {customer_id}")

    # ----------------------------
    # USER BEHAVIOR
    # ----------------------------

    user_search = search[search["customer_id"] == customer_id]
    user_wishlist = wishlist[wishlist["customer_id"] == customer_id]
    user_visits = visits[visits["customer_id"] == customer_id]

    interested_props = set(user_search["property_id"]) | \
                       set(user_wishlist["property_id"]) | \
                       set(user_visits["property_id"])

    if len(interested_props) == 0:
        print("No user behavior found → Showing general best properties")
        return

    user_df = df[df["property_id"].isin(interested_props)]

    # ----------------------------
    # LEARN PREFERENCES
    # ----------------------------

    avg_price = user_df["price"].mean()
    avg_size = user_df["house_size_sqft"].mean()
    preferred_state = user_df["state"].mode()[0]

    print(f"\nLearned Preferences:")
    print(f"→ Preferred Price: {int(avg_price)}")
    print(f"→ Preferred Size: {int(avg_size)}")
    print(f"→ Preferred State: {preferred_state}")

    # ----------------------------
    # SOFT FILTER
    # ----------------------------

    df = df[
        (df["price"].between(0.5 * avg_price, 1.5 * avg_price)) &
        (df["house_size_sqft"].between(0.5 * avg_size, 1.5 * avg_size))
    ]

    if df.empty:
        print("No matching properties found after filtering")
        return

    # ----------------------------
    # NORMALIZATION
    # ----------------------------

    df["price_score"] = (df["price"].max() - df["price"]) / (df["price"].max() - df["price"].min())

    df["size_score"] = (df["house_size_sqft"] - df["house_size_sqft"].min()) / \
                       (df["house_size_sqft"].max() - df["house_size_sqft"].min())

    df["safety_score"] = (df["crime_rate_index"].max() - df["crime_rate_index"]) / \
                         (df["crime_rate_index"].max() - df["crime_rate_index"].min())

    # ----------------------------
    # LOCATION
    # ----------------------------

    df["location_score"] = (
        0.5 * (1 / (df["metro_distance_km"] + 1)) +
        0.3 * (1 / (df["nearby_schools_km"] + 1)) +
        0.2 * (1 / (df["nearby_hospitals_km"] + 1))
    )

    # ----------------------------
    # STATE PREFERENCE
    # ----------------------------

    df["state_score"] = (df["state"] == preferred_state).astype(int)

    # ----------------------------
    # USER BEHAVIOR ANALYSIS
    # ----------------------------

    #Counts unique number of states user interacted with
    state_variety = user_df["state"].nunique()

    '''Standard deviation → measures spread of values
    for example 30L, 32L, 31L → low variation
    20L, 50L, 1cr → high variation
    Does user explore different price ranges?'''
    price_variation = user_df["price"].std()

    size_variation = user_df["house_size_sqft"].std()

    if state_variety == 1:
        diversity_weight = 0.02
    elif state_variety <= 3:
        diversity_weight = 0.04
    else:
        diversity_weight = 0.06

    print("\nUser Behavior Analysis:")
    print("State Variety:", state_variety)
    print("Price Variation:", int(price_variation))
    print("Size Variation:", int(size_variation))
    print("Diversity Weight:", diversity_weight)

    # -------------------
    # SMART DIVERSITY 
    # -------------------

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

    # ----------------------------
    # FINAL SCORE
    # ----------------------------

    df["final_score"] = (
        0.25 * df["price_score"] +
        0.20 * df["size_score"] +
        0.25 * df["location_score"] +
        0.20 * df["safety_score"] +
        0.05 * df["state_score"] +
        diversity_weight * (
            df["state_diversity"] +
            df["price_diversity"] +
            df["size_diversity"]
        )
    )

    # ----------------------------
    # OUTPUT
    # ----------------------------

    top = df.sort_values(by="final_score", ascending=False).head(10)

    print("\n---------- SMART RECOMMENDATIONS -----------")
    print(top[[
        "property_id",
        "state",
        "price",
        "house_size_sqft",
        "final_score"
    ]])