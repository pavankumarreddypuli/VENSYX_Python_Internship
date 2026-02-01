from utils.file_readers import read_csv, read_txt
from utils.docstream import stream_documents
from core.models import ScreenTime, AppUsage
from core.analyzer import Analyzer
from core.insights import Insights

RISKY_SITES = ["youtube.com", "facebook.com", "snapchat.com", "tiktok.com"]

analyzer = Analyzer()
insights = Insights()

def process_week(week_path, week_name):
    # Read raw files
    screen_raw = read_csv(f"{week_path}/screen_time.csv")
    app_raw = read_csv(f"{week_path}/app_usage.csv")
    browsing_raw = read_txt(f"{week_path}/browsing.txt")

    # Convert to objects
    screen_data = [ScreenTime(r["date"], r["minutes"]) for r in screen_raw]
    app_data = [AppUsage(r["app"], r["category"], r["minutes"]) for r in app_raw]

    # Stream browsing data
    sites = list(stream_documents(browsing_raw))

    # Analyze
    avg = analyzer.average_screen_time(screen_data)
    category = analyzer.top_category(app_data)
    risky = analyzer.risky_sites_count(sites, RISKY_SITES)

    # Print weekly insights
    insights.generate(week_name, avg, category, risky)

    # Return results for comparison
    return {
        "avg": avg,
        "category": category,
        "risky": risky
    }

# -------- PROCESS BOTH WEEKS --------

week1_result = process_week("data/week1", "Week 1")
week2_result = process_week("data/week2", "Week 2")

# -------- COMPARE WEEKS --------

insights.compare_weeks(week1_result, week2_result)
