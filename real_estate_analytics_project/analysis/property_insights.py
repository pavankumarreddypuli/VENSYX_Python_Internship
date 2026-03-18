from load_data import load_datasets

# Load all datasets
properties, customers, search, wishlist, visits, contact = load_datasets()

#Best Overall Properties

def best_properties():

    df = properties.copy()

    # 1. Normalize Features

    '''Cheap → 1 (best)
       Expensive → 0 (worst)'''
    
    df["price_score"] = (df["price"].max() - df["price"]) / (df["price"].max() - df["price"].min())

    df["size_score"] = (df["house_size_sqft"] - df["house_size_sqft"].min()) / \
                       (df["house_size_sqft"].max() - df["house_size_sqft"].min())

    df["bedroom_score"] = (df["bedrooms"] - df["bedrooms"].min()) / \
                          (df["bedrooms"].max() - df["bedrooms"].min())

    df["bathroom_score"] = (df["bathrooms"] - df["bathrooms"].min()) / \
                           (df["bathrooms"].max() - df["bathrooms"].min())

    df["parking_score"] = (df["parking_spaces"] - df["parking_spaces"].min()) / \
                          (df["parking_spaces"].max() - df["parking_spaces"].min())

    # Lower distance = better
    df["location_score"] = (df["metro_distance_km"].max() - df["metro_distance_km"]) / \
                           (df["metro_distance_km"].max() - df["metro_distance_km"].min())

    # Lower crime = better
    df["safety_score"] = (df["crime_rate_index"].max() - df["crime_rate_index"]) / \
                         (df["crime_rate_index"].max() - df["crime_rate_index"].min())

    # 2. Assign Weights (IMPORTANT)

    weights = {
        "price_score": 0.25,
        "size_score": 0.20,
        "location_score": 0.20,
        "safety_score": 0.15,
        "bedroom_score": 0.10,
        "bathroom_score": 0.05,
        "parking_score": 0.05
    }

    # 3. Final Score
    df["total_score"] = (
        df["price_score"] * weights["price_score"] +
        df["size_score"] * weights["size_score"] +
        df["location_score"] * weights["location_score"] +
        df["safety_score"] * weights["safety_score"] +
        df["bedroom_score"] * weights["bedroom_score"] +
        df["bathroom_score"] * weights["bathroom_score"] +
        df["parking_score"] * weights["parking_score"]
    )

    # 4. Ranking
    top = df.sort_values(by="total_score", ascending=False).head(5)

    print("\n----------------Top 5 Best Properties (Production Model--------------)")
    print(top[["property_id", "state", "price", "total_score"]])


#Best Budget Properties

'''Instead of: "Which house is cheap?"
   We ask: "Which house gives best value for money?'''

def best_budget_properties():

    df = properties.copy()

    #CLEAN DATA
    df = df[df["price"] > 0]
    df = df[df["house_size_sqft"] > 0]

    # Calculate price per sqft
    df["price_per_sqft"] = df["price"] / df["house_size_sqft"]

    best = df.sort_values(by="price_per_sqft").head(5)

    print("\n------------------Best Budget Properties----------------")
    print(best[["property_id", "price", "house_size_sqft", "price_per_sqft"]])


#Best Location Properties

def best_location_properties():

    df = properties.copy()
    
    df["location_score"] = (
       0.5 * (1 / (df["metro_distance_km"] + 1)) +
        0.3 * (1 / (df["nearby_schools_km"] + 1)) +
        0.2 * (1 / (df["nearby_hospitals_km"] + 1))
    )

    best = df.sort_values(by="location_score", ascending=False).head(5)

    #Highest score = best location
    print("\n---------------Best Location Properties-------------")
    print(best[["property_id", "metro_distance_km", "location_score"]])


#Safest Properties
def safest_properties():

    df = properties.copy()

    best = df.sort_values(by=["crime_rate_index", "metro_distance_km"]).head(5)

    print("\n-----------------Safest Properties---------------")
    print(best[["property_id", "crime_rate_index","metro_distance_km"]])


#Best Family Properties
def best_family_properties():

    df = properties.copy()

    best = df[
        (df["bedrooms"] >= 3) &
        (df["bathrooms"] >= 2) &
        (df["nearby_schools_km"] < 5)
    ].head(5)

    print("\n------------------Best Family Properties---------------")
    print(best[["property_id", "bedrooms", "bathrooms", "nearby_schools_km"]])



def best_hybrid_properties():

    df = properties.copy()

    # 1. DATA CLEANING
    df = df[(df["price"] > 0) & (df["house_size_sqft"] > 0)]

    # 2. NORMALIZATION (0–1)

    # Price (lower is better)
    df["price_score"] = (df["price"].max() - df["price"]) / (df["price"].max() - df["price"].min())

    # Size (higher is better)
    df["size_score"] = (df["house_size_sqft"] - df["house_size_sqft"].min()) / \
                       (df["house_size_sqft"].max() - df["house_size_sqft"].min())

    # Safety (lower crime better)
    df["safety_score"] = (df["crime_rate_index"].max() - df["crime_rate_index"]) / \
                         (df["crime_rate_index"].max() - df["crime_rate_index"].min())

    # Location components
    df["metro_score"] = 1 / (df["metro_distance_km"] + 1)
    df["school_score"] = 1 / (df["nearby_schools_km"] + 1)
    df["hospital_score"] = 1 / (df["nearby_hospitals_km"] + 1)

    # Weighted location score
    df["location_score"] = (
        0.5 * df["metro_score"] +
        0.3 * df["school_score"] +
        0.2 * df["hospital_score"]
    )

    # 3. FINAL HYBRID WEIGHTS

    weights = {
        "price": 0.25,
        "size": 0.20,
        "location": 0.30,
        "safety": 0.25
    }

    # 4. FINAL SCORE

    df["final_score"] = (
        df["price_score"] * weights["price"] +
        df["size_score"] * weights["size"] +
        df["location_score"] * weights["location"] +
        df["safety_score"] * weights["safety"]
    )
    # 5. RANKING

    top = df.sort_values(by="final_score", ascending=False).head(5)

    print("\n----------- HYBRID BEST PROPERTIES ---------------")
    print(top[[
        "property_id",
        "price",
        "house_size_sqft",
        "crime_rate_index",
        "location_score",
        "final_score"
    ]])   