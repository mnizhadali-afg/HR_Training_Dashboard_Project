# HR Training Dashboard Project


[![Python](https://img.shields.io/badge/Python-3.12.6-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![API](https://img.shields.io/badge/API-PetFinder-green.svg)](https://www.petfinder.com/developers/)
[![Cloud](https://img.shields.io/badge/Cloud-GCP-blue.svg)](https://cloud.google.com/)
[![Database](https://img.shields.io/badge/Database-BigQuery-orange.svg)](https://cloud.google.com/bigquery)
[![Automation](https://img.shields.io/badge/Automation-GitHub_Actions-yellow.svg)](https://github.com/features/actions)
[![Orchestration](https://img.shields.io/badge/Orchestration-Terraform-purple.svg)](https://www.terraform.io/)
[![Transformation](https://img.shields.io/badge/Transformation-DBT-red.svg)](https://www.getdbt.com/)
[![Visualization](https://img.shields.io/badge/Visualization-Looker-pink.svg)](https://cloud.google.com/looker)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)](https://github.com/)

## Goal
Simulate improving and automating a hypothetical internal process (e.g., tracking training completion, feedback, or participant engagement) and visualize its performance. This project directly touches upon data integration, automation, visualization, and process thinking, with a strong link to your lecturing background.

## Scenario
Imagine a company has a global training department (like the one in the "Education Expert IT" role). They manually track course completion, participant feedback, and engagement across various platforms (some old, some new). Your task is to automate this, centralize the data, and provide insights.

## KPIs
1. **Course Completion Rate:** (Percentage of enrolled users who completed a course)
2. **Average Course Feedback Score**: (Overall satisfaction with courses)
3. **Active Participant Count:** (Number of unique users engaging with training each month/quarter)
4. **Training Hours Delivered:** (Total hours of training provided)

## Technologies Used
* **Python** (for data generation, ETL, and API)
    * Libraries: `pandas`, `Flask`, `csv`
* **PostgreSQL** (for database - to be set up on Day 4)
* **Docker** (for PostgreSQL - to be used on Day 4)
* **Tableau Public / Power BI Desktop** (for dashboarding - to be used in Week 2)
* **Git & GitHub** (for version control)
* **JSON** (data format for API)

## Initial Data Sources
* `data/raw/participants.csv`: Contains participant demographic information.
* `data/raw/courses.csv`: Contains details about training courses.
* `data/raw/enrollments.csv`: Records participant enrollments, completion status, and scores.
* `data/raw/feedbacks.csv`: Stores feedback ratings and comments for enrollments.
* **API Endpoint (`api/api.py`):** Serves `engagements` data in JSON format.
    * Base URL: `http://127.0.0.1:5000/`
    * Engagements Endpoint: `http://127.0.0.1:5000/api/engagements`
    * To run the API: Navigate to the `api/` directory (after activating virtual environment) and execute `python api.py`.

## Project Structure

 Career guide

Excellent! Glad to hear Day 3 went smoothly. Having a running API is a significant step.

Yes, absolutely! You should definitely update your README.md file.

The README.md is your project's living documentation and its primary showcase. It should always reflect the current state of your project and its capabilities.

Action: Update README.md for Day 3

Goal: Reflect the addition of your dummy API as a data source and the new technologies introduced.

How to Update Your README.md:

    Open your README.md file in your project's root directory.

    Add a "Technologies Used" or "Tech Stack" section:
        If you don't have one, create it.
        If you do, update it to include:
            Python
            Flask (or FastAPI, depending on what you used)
            pandas
            csv (Python built-in, but good to note its use for data generation)
        You can also mention JSON as a data format.

    Update "Data Sources" section:
        Clearly mention that your engagements data is now served via a Flask REST API.
        You can even include the local endpoint URL (e.g., http://127.0.0.1:5000/api/engagements) as an example of how to access it.
        Reiterate that participants.csv, courses.csv, enrollments.csv, and feedbacks.csv are flat files.

    Add "API Setup and Usage" instructions:
        Briefly explain how to run your api.py (e.g., "Navigate to the api/ directory and run python api.py").
        Mention the base URL (http://127.0.0.1:5000/) and the engagement endpoint.

    Reflect your progress:
        You could add a small "Progress" section or a bullet point under "Project Overview" noting that "Initial data generation (CSV) and a dummy API for engagement data have been set up."

Example Snippets to Add/Update:
Markdown

# HR Training Dashboard Project

## Project Overview
This project aims to build an automated data pipeline and dashboard to visualize key performance indicators (KPIs) for internal HR/Training programs. It involves integrating data from various simulated sources, transforming it, and presenting it through an interactive dashboard.

## Key Performance Indicators (KPIs)
* Course Completion Rate
* Average Course Feedback Score
* Active Participant Count
* Training Hours Delivered

## Technologies Used
* **Python** (for data generation, ETL, and API)
    * Libraries: `pandas`, `Flask`, `csv`
* **PostgreSQL** (for database - to be set up on Day 4)
* **Docker** (for PostgreSQL - to be used on Day 4)
* **Tableau Public / Power BI Desktop** (for dashboarding - to be used in Week 2)
* **Git & GitHub** (for version control)
* **JSON** (data format for API)

## Initial Data Sources
* `data/raw/participants.csv`: Contains participant demographic information.
* `data/raw/courses.csv`: Contains details about training courses.
* `data/raw/enrollments.csv`: Records participant enrollments, completion status, and scores.
* `data/raw/feedbacks.csv`: Stores feedback ratings and comments for enrollments.
* **API Endpoint (`api/api.py`):** Serves `engagements` data in JSON format.
    * Base URL: `http://127.0.0.1:5000/`
    * Engagements Endpoint: `http://127.0.0.1:5000/api/engagements`
    * To run the API: Navigate to the `api/` directory (after activating virtual environment) and execute `python api.py`.

## Project Structure
---
HR_Training_Dashboard_Project/
├── api/
│   └── api.py                   # Flask application to serve dummy API data
├── data/
│   └── raw/
│       ├── participants.csv
│       ├── courses.csv
│       ├── enrollments.csv
│       ├── feedbacks.csv
│       └── engagements.csv      # Source for the API, but also a raw file
├── venv/                        # Python virtual environment
├── .gitignore                   # (Optional) Add 'venv/' here to ignore it in git
└── README.md                    # This file!

## Initial Data Schema
![Initial Data Schema](/data/images/schema.png)
