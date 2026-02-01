class ScreenTime:
    def __init__(self, date, minutes):
        self.date = date
        self.minutes = int(minutes)


class AppUsage:
    def __init__(self, app, category, minutes):
        self.app = app
        self.category = category
        self.minutes = int(minutes)




'''
Converts raw CSV rows into objects
Makes code clean & reusable
'''