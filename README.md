# HR Training Dashboard Project
---
## Project Overview
This project aims to build an automated data pipeline and dashboard to visualize key performance indicators (KPIs) for internal HR/Training programs. It involves integrating data from various simulated sources, transforming it, and presenting it through an interactive dashboard.

[![Python](https://img.shields.io/badge/Python-3.12.6-blue.svg)](https://www.python.org/)
<!-- [![Cloud](https://img.shields.io/badge/Cloud-GCP-blue.svg)](https://cloud.google.com/) -->
<!-- [![Database](https://img.shields.io/badge/Database-BigQuery-orange.svg)](https://cloud.google.com/bigquery) -->
[![Automation](https://img.shields.io/badge/Automation-GitHub_Actions-yellow.svg)](https://github.com/features/actions)
<!-- [![Orchestration](https://img.shields.io/badge/Orchestration-Terraform-purple.svg)](https://www.terraform.io/) -->
<!-- [![Transformation](https://img.shields.io/badge/Transformation-DBT-red.svg)](https://www.getdbt.com/) -->
<!-- [![Visualization](https://img.shields.io/badge/Visualization-Looker-pink.svg)](https://cloud.google.com/looker) -->
[![Status](https://img.shields.io/badge/Status-Active-green.svg)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

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
* **pgAdmin** (GUI for interacting with DB)
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
```
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
├── venv/ 
├── .env 
├── .gitignore                   
├── docker-compose.yml           
└── README.md                    # This file!
```

## Initial Data Schema
![Initial Data Schema](/data/images/schema.png)
