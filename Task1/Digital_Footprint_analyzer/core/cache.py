import json

# Save weekly analysis report into a JSON file
def save_report(week, report):
    # Create a file with week name
    with open(f"{week}_report.json", "w") as file:
        # Write report dictionary into JSON format
        json.dump(report, file)


