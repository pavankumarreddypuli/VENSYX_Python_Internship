from load_data import load_datasets

properties, customers, search, wishlist, visits, contact = load_datasets()


def recommend_properties(customer_id):

    df = properties.copy()

    print(f"\nRecommendations for Customer: {customer_id}")

    #GET CUSTOMER HISTORY

    user_search = search[search["customer_id"] == customer_id]
    user_wishlist = wishlist[wishlist["customer_id"] == customer_id]
    user_visits = visits[visits["customer_id"] == customer_id]

    #GET INTERESTED PROPERTIES

    interested_props = set(user_search["property_id"]) | \
                       set(user_wishlist["property_id"]) | \
                       set(user_visits["property_id"])

    if len(interested_props) == 0:
        print("No behavior data found, showing general best properties")
        return

    user_df = df[df["property_id"].isin(interested_props)]

    # 3. FIND PREFERRED PATTERN

    avg_price = user_df["price"].mean()
    avg_size = user_df["house_size_sqft"].mean()
    preferred_state = user_df["state"].mode()[0]

    print(f"Preferred Price: {int(avg_price)}")
    print(f"Preferred Size: {int(avg_size)}")
    print(f"Preferred State: {preferred_state}")

    # 4. FILTER SIMILAR PROPERTIES

    df = df[
        (df["price"].between(0.8 * avg_price, 1.2 * avg_price)) &
        (df["house_size_sqft"].between(0.8 * avg_size, 1.2 * avg_size)) &
        (df["state"] == preferred_state)
    ]

    if df.empty:
        print("No matching properties found!")
        return

    # 5. SCORING (HYBRID)

    df["price_score"] = (df["price"].max() - df["price"]) / (df["price"].max() - df["price"].min())
    df["size_score"] = (df["house_size_sqft"] - df["house_size_sqft"].min()) / \
                       (df["house_size_sqft"].max() - df["house_size_sqft"].min())

    df["safety_score"] = (df["crime_rate_index"].max() - df["crime_rate_index"]) / \
                         (df["crime_rate_index"].max() - df["crime_rate_index"].min())

    df["location_score"] = (
        0.5 * (1 / (df["metro_distance_km"] + 1)) +
        0.3 * (1 / (df["nearby_schools_km"] + 1)) +
        0.2 * (1 / (df["nearby_hospitals_km"] + 1))
    )

    df["final_score"] = (
        0.3 * df["price_score"] +
        0.25 * df["size_score"] +
        0.25 * df["location_score"] +
        0.2 * df["safety_score"]
    )

    # 6. FINAL RECOMMENDATIONS

    top = df.sort_values(by="final_score", ascending=False).head(5)

    print("\n-----------------Personalized Recommendations (Behavior-Based)------------------")
    print(top[[
        "property_id",
        "state",
        "price",
        "house_size_sqft",
        "final_score"
    ]])