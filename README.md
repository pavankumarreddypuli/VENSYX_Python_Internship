## 📊 Digital Footprint Analyzer (Privacy-Focused)

A fully offline, privacy-focused analytics engine that analyzes personal digital activity — including screen time, app usage, and browsing logs — to generate meaningful insights about productivity and online habits.

No data leaves your machine.  
No cloud uploads.  
Everything runs locally.

---

## 🚀 Features

### ✔ Offline Analytics
All analysis happens locally on your device.  
No internet connection or third-party services are required.

---

### ✔ Weekly Insights (Single Week)
For a given week, the system reads the following files:

- `screen_time.csv`
- `app_usage.csv`
- `browsing.txt`

And generates a clear summary report.

---

### ✔ Smart Insight Generation
The generated insights include:

- Average daily screen time  
- Most-used app category (Productivity / Social / Entertainment, etc.)  
- Number of risky website visits  

Risky sites are detected using a predefined list:
- YouTube
- Facebook
- Snapchat
- TikTok

---

### ✔ Clean Modular Architecture
The project is designed for scalability and maintainability using:

- Object-Oriented Programming (OOP) models  
- Encapsulated insight generation  
- Utility modules for file reading and streaming  
- Caching system to avoid repeated computation  

---

### ✔ Error Handling
Graceful handling of:
- Missing files  
- Invalid or malformed data  

Implemented using custom exception classes.

---

## 📁 Project Structure
```
digital_footprint_analyzer/
│
├── data/
│ └── week1/
│ ├── screen_time.csv
│ ├── app_usage.csv
│ └── browsing.txt
│
├── core/
│ ├── models.py
│ ├── analyzer.py
│ ├── insights.py
│ ├── cache.py
│ └── exceptions.py
│
├── utils/
│ ├── docstream.py
│ └── file_readers.py
│
├── cache/
│ └── week1.json # Auto-generated cache file
│
└── main.py

```
---

## 🧠 How It Works (Flow Summary)
```
1. User runs `main.py`
2. System checks if a cached report for the week exists
3. If cache is available:
   - Load insights directly from cache
4. Otherwise:
   - Read CSV and text files
   - Parse and clean data
   - Analyze screen time, app usage, and browsing activity
   - Generate insights
   - Save results to cache
5. Display the formatted weekly insight report

---
```
## 📄 Data Input Format
```csv
### 1️⃣ screen_time.csv
date,minutes
2026-01-01,320
2026-01-02,410
2026-01-03,290

2️⃣ app_usage.csv
app,category,minutes
YouTube,Entertainment,60
VSCode,Productivity,180
Instagram,Social,90

3️⃣ browsing.txt
youtube.com
instagram.com
stackoverflow.com
facebook.com
snapchat.com
```
## 📊 Example Output

--- Digital Footprint Insights ---
```
Average daily screen time: 354.3 minutes
High Productivity usage
Risky site visits: 3
```
## 🧩 Core Modules (Explanation)
🔶 core/models.py
```
Defines core data models:

ScreenTime

AppUsage

These models store structured data used for analysis.
```
🔶 core/analyzer.py
```
The main processing engine:

Loads and validates input data

Performs calculations

Returns computed insights
```
🔶 core/insights.py
```
Responsible for formatting and displaying:

Human-readable insight reports

Clean console output
```
🔶 core/cache.py
```
Handles caching of weekly analysis results:

Saves computed insights as JSON

Loads cached results if available
```
🔶 core/exceptions.py
```
Defines custom exceptions such as:

DataNotFoundError

CacheNotFoundError
```
🔶 utils/docstream.py
```
Implements generator-based streaming for memory-efficient data processing.
```
🔶 utils/file_readers.py
```
Provides reusable utilities for reading:

CSV files

Text files
```
🔶 main.py
```
The entry point of the application:

Loads or generates insights

Coordinates all modules

Displays the final report
```
## ⚠️ Important Notes
```
If you modify insight field names, delete old cache files inside /cache/

Ensure CSV files follow the correct format

The system runs completely offline
```
## 👨‍💻 Author
```
Pavan Kumar Reddy Puli
Python Intern

