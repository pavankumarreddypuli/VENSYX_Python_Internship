from core.models import ScreenTime, AppUsage

# Analyzer class performs all calculations
class Analyzer:

    # Calculate average daily screen time
    def average_screen_time(self, screen_data):
        # Sum total minutes from all ScreenTime objects
        total_minutes = sum(item.minutes for item in screen_data)
        
        # Calculate and return average (rounded to 1 decimal)
        return round(total_minutes / len(screen_data), 1)

    # Find which app category has highest total usage
    def top_category(self, app_data):
        # Dictionary to store total minutes per category
        category_map = {}

        # Loop through each AppUsage object
        for app in app_data:
            # Add minutes to the corresponding category
            category_map[app.category] = category_map.get(app.category, 0) + app.minutes

        # Return category with maximum usage time
        return max(category_map, key=category_map.get)

    # Count how many risky websites were visited
    def risky_sites_count(self, sites, risky):
        # Count sites that exist in the risky list
        return sum(1 for site in sites if site in risky)
