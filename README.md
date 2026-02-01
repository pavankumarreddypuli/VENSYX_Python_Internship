# 🕵️ Digital Footprint Analyzer
## Privacy-Focused Offline Analytics System

-------------------------------------------------------------------------------------------

## 🧩 What Is This Task?

This project is an **offline data analytics task** that analyzes a user’s **digital activity logs** (screen time, app usage, and browsing history) stored as local files and generates **meaningful insights** without sending any data to external servers.

--------------------------------------------------------------------------------------------

## 📌 Problem Statement

In the modern digital environment, users spend a large amount of time on screens, applications, and websites without understanding how it affects their productivity, privacy, and digital well-being.  
Most existing analytics tools collect and transmit personal data to external servers, which introduces **privacy and security risks**.

👉 The challenge is to **analyze digital activity locally**, ensure **user privacy**, and still provide **useful behavioral insights**.

--------------------------------------------------------------------------------------------------------

## 💡 Solution Overview

This project provides a **privacy-first, offline solution** that:

- Reads user activity logs from **CSV and TXT files**
- Converts raw data into structured Python objects using **OOP**
- Uses **generators** to efficiently process browsing data
- Computes weekly digital behavior metrics
- Compares activity between **Week 1 and Week 2**
- Generates clear, human-readable insights in the console

---------------------------------------------------------------------------------------------------------

## 🎯 Objectives

- Analyze weekly digital activity logs stored locally  
- Calculate:
  - Average daily screen time  
  - Most used application category  
  - Number of risky website visits  
- Compare digital behavior between two weeks  
- Ensure the entire system works **offline**  
- Follow a **clean, modular, and scalable architecture**

--------------------------------------------------------------------------------------------------

## 📁 Project Structure & Workflow

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


-------------------------------------------------------------------------------------------

### 📂 `data/`
Stores raw weekly digital activity data files.

- `week1/` – User activity logs for Week 1  
- `week2/` – User activity logs for Week 2  

### 📄 `screen_time.csv`
Stores daily screen usage data.

### 📄 `app_usage.csv`
Stores application usage data categorized by type.

### 📄 `browsing.txt`
Stores visited websites used to identify risky browsing behavior.

---

### 📂 `core/`

- `models.py` – Defines OOP models to represent screen time and app usage data  
- `analyzer.py` – Performs all calculations and analytics logic  
- `insights.py` – Generates readable weekly insights and comparisons  
- `cache.py` – Caches computed reports for future scalability  
- `exceptions.py` – Handles custom exceptions for missing or invalid data  

---

### 📂 `utils/`

- `file_readers.py` – Safely reads CSV and TXT files  
- `docstream.py` – Streams browsing data using Python generators  

---

### 📄 `main.py`

Acts as the **entry point** that connects all modules and executes the complete workflow.

--------------------------------------------------------------------------------------------------------

## 🔁 End-to-End Workflow

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

--------------------------------------------------------------------------------------------------

## 📈 Outcomes

- Clear understanding of user screen usage patterns  
- Identification of dominant application categories  
- Detection of risky browsing habits  
- Week-wise behavioral comparison  
- Fully offline and privacy-preserving analytics  

--------------------------------------------------------------------------------------------------

## ▶️ How to Run the Project

1. Ensure **Python 3.x** is installed
2. Open the project folder in **VS Code**
3. Run the following command from the root directory:

```bash
python main.py

------------------------------------------------------------------------------------------------------
🖥️ Example Output

📊 DIGITAL FOOTPRINT ANALYSIS REPORT

Week 1:
- Average Daily Screen Time: 5.4 hours
- Most Used App Category: Social Media
- Risky Website Visits: 6

Week 2:
- Average Daily Screen Time: 4.8 hours
- Most Used App Category: Productivity
- Risky Website Visits: 2

📈 Comparison Insights:
- Screen time decreased by 0.6 hours
- Shift from Social Media to Productivity apps
- Risky browsing behavior reduced significantly

