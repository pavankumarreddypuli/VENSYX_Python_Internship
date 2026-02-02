from utils.file_readers import read_csv, read_txt
from utils.docstream import stream_documents
from core.models import ScreenTime, AppUsage
from core.analyzer import Analyzer
from core.insights import Insights

RISKY_SITES = ["youtube.com", "facebook.com", "snapchat.com", "tiktok.com"]

# Read files
screen_raw = read_csv("data/week1/screen_time.csv")
app_raw = read_csv("data/week1/app_usage.csv")
browsing_raw = read_txt("data/week1/browsing.txt")

# Convert to objects
screen_data = [
    ScreenTime(row["date"], row["minutes"]) 
    for row in screen_raw
]
app_data = [
    AppUsage(row["app"], row["category"], row["minutes"]) 
    for row in app_raw
]

# Stream browsing data
browsing_sites = list(stream_documents(browsing_raw))

# Analyze
analyzer = Analyzer()
avg_time = analyzer.average_screen_time(screen_data)
top_category = analyzer.top_category(app_data)
risky_count = analyzer.risky_sites_count(browsing_sites, RISKY_SITES)

# Show insights
Insights().generate(avg_time, top_category, risky_count)
