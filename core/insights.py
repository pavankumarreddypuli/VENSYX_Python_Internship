# Insights class prints reports and comparisons
class Insights:

    def generate(self, week, avg_time, top_category, risky_count):
        print(f"\n--- {week} Digital Footprint Insights ---")
        print(f"Average daily screen time: {avg_time} minutes")
        print(f"High {top_category} usage")
        print(f"Risky site visits: {risky_count}")

    # Compare two weeks and show trend
    def compare_weeks(self, w1, w2):
        print("\n--- Week Comparison ---")

        # Screen time comparison
        if w2["avg"] > w1["avg"]:
            print("📈 Screen time increased in Week2")
        else:
            print("📉 Screen time decreased in Week2")

        # Category comparison
        if w1["category"] == w2["category"]:
            print(f"➡️ Same dominant category: {w1['category']}")
        else:
            print(f"🔄 Category changed from {w1['category']} to {w2['category']}")

        # Risky site comparison
        diff = w2["risky"] - w1["risky"]
        print(f"⚠️ Risky site visits change: {diff}")
