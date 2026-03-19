import property_insights
import customer_recommendation
import customer_new_recommendation
from load_data import load_datasets

# Load datasets
properties, customers, search, wishlist, visits, contact = load_datasets()

property_insights.best_properties()
property_insights.best_budget_properties()
property_insights.best_location_properties()
property_insights.safest_properties()
property_insights.best_family_properties()
property_insights.best_hybrid_properties()
# Example customer
customer_recommendation.recommend_properties("C0000001")
customer_new_recommendation.recommend_properties("C0000001")
