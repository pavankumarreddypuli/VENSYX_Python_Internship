from load_data import load_datasets

# Load data
properties, customers, search, wishlist, visits, contact = load_datasets()


def recommend_properties(customer_id):

    df = properties.copy()

    # ----------------------------
    # 1. GET CUSTOMER DATA
    # ----------------------------
    customer = customers[customers["customer_id"] == customer_id]

    if customer.empty:
        print("Customer not found!")
        return

    customer = customer.iloc[0]

    budget = customer["budget"]
    preferred_state = customer["preferred_state"]
    family_size = customer["family_size"]

    print(f"\nRecommendations for Customer: {customer_id}")
    print(f"Budget: {budget}, State: {preferred_state}, Family Size: {family_size}")

    # ----------------------------
    # 2. FILTER BASED ON CUSTOMER
    # ----------------------------

    # Budget filter (within 20% range)
    df = df[(df["price"] >= 0.8 * budget) & (df["price"] <= 1.2 * budget)]

    # Location preference
    df = df[df["state"] == preferred_state]

    # Family size → bedrooms
    df = df[df["bedrooms"] >= family_size]

    if df.empty:
        print("No matching properties found!")
        return

    # ----------------------------
    # 3. NORMALIZATION
    # ----------------------------

    df["price_score"] = (df["price"].max() - df["price"]) / (df["price"].max() - df["price"].min())

    df["size_score"] = (df["house_size_sqft"] - df["house_size_sqft"].min()) / \
                       (df["house_size_sqft"].max() - df["house_size_sqft"].min())

    df["safety_score"] = (df["crime_rate_index"].max() - df["crime_rate_index"]) / \
                         (df["crime_rate_index"].max() - df["crime_rate_index"].min())

    # Location scoring
    df["location_score"] = (
        0.5 * (1 / (df["metro_distance_km"] + 1)) +
        0.3 * (1 / (df["nearby_schools_km"] + 1)) +
        0.2 * (1 / (df["nearby_hospitals_km"] + 1))
    )

    # ----------------------------
    # 4. PERSONALIZED WEIGHTS
    # ----------------------------

    weights = {
        "price": 0.30,
        "size": 0.25,
        "location": 0.25,
        "safety": 0.20
    }

    # ----------------------------
    # 5. FINAL SCORE
    # ----------------------------

    df["final_score"] = (
        df["price_score"] * weights["price"] +
        df["size_score"] * weights["size"] +
        df["location_score"] * weights["location"] +
        df["safety_score"] * weights["safety"]
    )

    # ----------------------------
    # 6. TOP RECOMMENDATIONS
    # ----------------------------

    top = df.sort_values(by="final_score", ascending=False).head(5)

    print("\n🔥 Personalized Recommendations 🔥")
    print(top[[
        "property_id",
        "state",
        "price",
        "bedrooms",
        "location_score",
        "final_score"
    ]])