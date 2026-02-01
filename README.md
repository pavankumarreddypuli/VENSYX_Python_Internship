# 🕵️ Digital Footprint Analyzer
### Privacy-Focused Offline Analytics System

---------------------------------------------------------------------------------

## 📌 Problem Statement

In today’s digital world, users spend a significant amount of time on screens, applications, and websites, often without realizing their impact on productivity, privacy, and digital well-being.  
Most analytics tools send personal data to external servers, raising serious privacy concerns.

👉 The goal of this project is to analyze a user’s digital activity **locally**, without sending data anywhere, and provide **meaningful insights** about screen usage, application behavior, and risky browsing habits.

---

##  Objectives

This project aims to:

- Analyze weekly digital activity logs stored as files  
- Compute:
  - Average daily screen time  
  - Most used application category  
  - Number of risky website visits  
- Compare digital behavior between **Week 1** and **Week 2**  
- Generate insights **offline using Python**  
- Follow a **clean, scalable, and modular architecture**

---

##  Features Implemented

- Scalable and modular folder architecture  
- Object-Oriented Programming (OOP) for data modeling  
- File handling for CSV and TXT files  
- Memory-efficient data streaming using generators  
- Weekly analytics and behavior comparison  
- Fully offline processing (privacy-focused)   

----------------------------------------------------------------------------
##  Project Structure

digital_footprint_analyzer/
│
├── data/
│ ├── week1/
│ │ ├── screen_time.csv
│ │ ├── app_usage.csv
│ │ └── browsing.txt
│ └── week2/
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
│ ├── file_readers.py
│ └── docstream.py
│
└── main.py

--------------------------------------------------------------------------------

---

##  Module Overview

###  `data/`
Stores weekly raw digital activity logs.

- `week1/` – Week 1 user activity data  
- `week2/` – Week 2 user activity data  

---

###  `core/models.py`
Defines OOP data models such as `ScreenTime` and `AppUsage` for structured representation.

---

### 🔹 `core/analyzer.py`
Contains core business logic to calculate:
- Average screen time  
- Dominant application category  
- Risky website visit counts  

---

###  `core/insights.py`
Generates readable weekly insights and compares **Week 1 vs Week 2** behavior.

---

###  `core/cache.py`
Caches generated reports to avoid recomputation and support future scalability.

---

###  `core/exceptions.py`
Handles custom exceptions for missing, corrupted, or invalid data.

---

###  `utils/file_readers.py`
Centralized utility for safely reading CSV and TXT files.

---

###  `utils/docstream.py`
Uses Python generators to stream browsing data efficiently.

---

###  `main.py`
Main entry point that connects all modules and executes the analysis workflow.

---
-------------------------------------------------------------------------------------------------

##  Workflow
User Activity Files (CSV / TXT)
↓
File Readers (utils)
↓
Data Models (OOP)
↓
Analyzer (Calculations)
↓
Insights Generator
↓
Week 1 vs Week 2 Comparison
↓
Final Output in Console
---------------------------------------------------------------------------------------------------

##  How It Works (Simple Steps)

1. Reads screen time, app usage, and browsing history files  
2. Converts raw data into Python objects using OOP  
3. Streams browsing history using generators  
4. Calculates:
   - Average screen time  
   - Most used application category  
   - Risky website visits  
5. Generates weekly insights  
6. Compares Week 1 and Week 2 behavior  
7. Displays results in a clean, readable console output  

---

##  Privacy First

- No internet connection required  
- No data sent to external servers  
- All analysis happens locally  

---

##  How to Run

```bash
python main.py


