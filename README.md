🕵️ Digital Footprint Analyzer

(Privacy-Focused Offline Analytics System)

📌 Problem Statement

In today’s digital world, users spend a significant amount of time on screens, applications, and websites, often without realizing their impact on productivity, privacy, and digital well-being.
Most analytics tools send personal data to external servers, raising privacy concerns.

👉 The problem is to analyze a user’s digital activity locally, without sending data anywhere, and provide meaningful insights about screen usage, application behavior, and risky browsing habits.

🎯 Task / Objective

The main task of this project is to:

Analyze weekly digital activity logs stored as files

Compute:

Average daily screen time

Most used application category

Number of risky website visits

Compare digital behavior between Week1 and Week2

Generate insights offline using Python

Follow a clean, scalable, and modular architecture

✅ What I Did in This Project

Designed a scalable folder architecture

Used Object-Oriented Programming (OOP) to model data

Implemented file handling for CSV and TXT files

Applied generators for memory-efficient streaming

Performed weekly analytics and comparisons

Ensured the solution works offline (privacy-focused)

Made the project VS Code and GitHub ready

📁 Project Structure & One-Line Explanation (VERY IMPORTANT)
digital_footprint_analyzer/

🔹 data/

Stores weekly raw digital activity data files.

week1/ – Contains Week 1 user activity logs

week2/ – Contains Week 2 user activity logs

🔹 core/models.py

Defines OOP models (ScreenTime, AppUsage) to represent structured data.

🔹 core/analyzer.py

Contains core business logic for calculating averages, categories, and risky site counts.

🔹 core/insights.py

Generates readable weekly insights and compares Week1 vs Week2 trends.

🔹 core/cache.py

Stores generated weekly reports to avoid recomputation (future scalability).

🔹 core/exceptions.py

Handles custom exceptions for missing or invalid data.

🔹 utils/file_readers.py

Centralized utility to read CSV and text files safely.

🔹 utils/docstream.py

Uses Python generators to stream browsing data efficiently.

🔹 main.py

Main entry point that connects all modules and executes the workflow.

🔁 Overall Workflow (End-to-End)
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
Week1 vs Week2 Comparison
            ↓
Final Output in Console

🧠 Workflow Explained in Simple Steps

Read screen time, app usage, and browsing history files

Convert raw data into Python objects using OOP

Stream browsing data using generators

Calculate:

Average screen time

Dominant app category

Risky website visits

Generate insights for each week

Compare Week1 and Week2 to detect behavioral trends

Display results in a clean, readable format
