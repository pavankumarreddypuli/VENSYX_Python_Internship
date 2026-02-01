from core.models import ScreenTime, AppUsage

class Analyzer:

    def average_screen_time(self, screen_data):
        # Sum total minutes from all ScreenTime objects
        total = sum(item.minutes for item in screen_data)
        # Calculate and return average (rounded to 1 decimal)
        return round(total / len(screen_data), 1)
    
    # Find which app category has highest total usage
    def top_category(self, app_data):
        category_map = {}

        for app in app_data:
            category_map[app.category] = category_map.get(app.category, 0) + app.minutes

        return max(category_map, key=category_map.get)
    
    # Count how many risky websites were visited
    def risky_sites_count(self, sites, risky):
        return sum(1 for site in sites if site in risky)
