# This class represents one day of screen time data
class ScreenTime:
    def __init__(self, date, minutes):
        self.date = date
        self.minutes = int(minutes)


# This class represents usage of a single app
class AppUsage:
    def __init__(self, app, category, minutes):
        self.app = app
        self.category = category
        self.minutes = int(minutes)
