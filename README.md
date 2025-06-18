# 📈 HR Training Dashboard Project: [From Raw Data to Actionable Insights]

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-26.1.4-blue.svg?logo=docker&logoColor=white)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1.svg?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-2.130.820.0-F2C811.svg?logo=powerbi&logoColor=white)](https://powerbi.microsoft.com/)
[![Pandas](https://img.shields.io/badge/pandas-2.2.2-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0.30-336699.svg?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![Psycopg2](https://img.shields.io/badge/psycopg2-2.9.9-006400.svg?logo=postgresql&logoColor=white)](https://pypi.org/project/psycopg2-binary/)
[![python-dotenv](https://img.shields.io/badge/python--dotenv-1.0.1-F7DF1E.svg?logo=python&logoColor=white)](https://pypi.org/project/python-dotenv/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## ✨ Project Overview

This project showcases the end-to-end development of an HR Training Dashboard. Starting with raw CSV data, it establishes a robust data pipeline using Docker, PostgreSQL, and Python for ETL processes, culminating in an interactive dashboard built with Power BI. The unique aspect of this project is its successful implementation across a **dual-boot Linux and Windows environment**, simulating a common real-world scenario where development environments might differ from analytical ones.

The dashboard provides key performance indicators (KPIs) and insights into training effectiveness, participant engagement, and resource allocation within an HR training program.

## 🚀 Key Features

- **Data Pipeline Automation:** Python scripts for seamless ingestion and transformation of raw training data.
- **Containerized Database:** PostgreSQL and pgAdmin orchestrated with Docker Compose for isolated and efficient data management.
- **Robust ETL Process:** Data cleaning, enrichment, and transformation into a star-schema-friendly `fact_training_kpis` table.
- **Interactive Power BI Dashboard:** Dynamic visualizations of crucial HR training KPIs.
- **Cross-OS Compatibility:** Detailed setup instructions for both Linux (for pipeline execution) and Windows (for dashboard development).

## 📊 Key Performance Indicators (KPIs)

The dashboard focuses on the following critical metrics:

1.  **Course Completion Rate:** Percentage of completed training enrollments.
2.  **Average Course Feedback Score:** Participant satisfaction and training quality assessment.
3.  **Active Participant Count:** Unique individuals engaged in training programs over time.
4.  **Total Training Hours Delivered:** Overall investment and volume of training provided.

## 🛠️ Technologies Used

- **Operating Systems:** Linux (e.g., Ubuntu), Windows
- **Containerization:** Docker, Docker Compose
- **Database:** PostgreSQL
- **Database Management:** pgAdmin
- **Programming Language:** Python 3
- **Python Libraries:** `pandas`, `sqlalchemy`, `psycopg2-binary`, `python-dotenv`
- **Business Intelligence:** Microsoft Power BI Desktop
- **Version Control:** Git

## 📂 Project Structure

```
HR_Training_Dashboard_Project/
├── api/
│   └── api.py                   # Flask application to serve dummy API data
├── data/
│   ├── raw/                     # Contains raw CSV data files
│   │   ├── participants.csv
│   │   ├── courses.csv
│   │   ├── enrollments.csv
│   │   ├── feedbacks.csv
│   │   └── engagements.csv
│   └── images/
│       └── schema.png           # Database schema diagram
│       └── dashboard_1.png      # Power BI Dashboard
│       └── dashboard_2.png      # Power BI Dashboard
│       └── dashboard_3.png      # Power BI Dashboard
├── etl/
│   └── load_initial_data.py     # Script to load initial raw CSVs into PostgreSQL
│   └── transform_data.py        # Script to load all required KPIs into a Fact Table in PostgreSQL
├── venv/                        # Python virtual environment
├── .env                         # Environment variables for sensitive data (e.g., DB credentials)
├── .gitignore                   # Specifies files/directories to ignore in Git
├── docker-compose.yml           # Defines Docker services (PostgreSQL, pgAdmin)
└── README.md                    # Project documentation
```

## ⚙️ Setup & Deployment Guide: A Dual-OS Journey

This project was developed by leveraging the strengths of both Linux for backend data processing and Windows for frontend visualization. Follow these phases carefully.

### **Phase 1: Setting up the Data Pipeline on Linux (Backend Processing)** 🐧

_(Assumes you have Git, Docker Engine, and Python 3 installed on your Linux distribution.)_

1.  **Clone the Repository:**
    Open your Linux terminal and clone the project, then navigate into its directory:

    ```bash
    git clone [https://github.com/YOUR_GITHUB_USERNAME/HR_Training_Dashboard_Project.git](https://github.com/YOUR_GITHUB_USERNAME/HR_Training_Dashboard_Project.git)
    cd HR_Training_Dashboard_Project
    ```

2.  **Configure Environment Variables (`.env` file):**
    Create a new file named `.env` in the root of the `HR_Training_Dashboard_Project/` directory. Fill it with your chosen database and pgAdmin credentials.

    ```env
    # .env file content
    POSTGRES_USER=your_postgres_user
    POSTGRES_PASSWORD=your_postgres_password
    POSTGRES_DB=your_database_name_e.g._hr_training_db
    PGADMIN_DEFAULT_EMAIL=your_pgadmin_email@example.com
    PGADMIN_DEFAULT_PASSWORD=your_pgadmin_password
    ```

3.  **Launch Database Services (Docker Compose):**
    Start your PostgreSQL database and pgAdmin containers in detached mode (`-d`):

    ```bash
    docker-compose up -d
    ```

    Verify that both services are running and healthy:

    ```bash
    docker-compose ps
    ```

    _(Expected output: Both `db` and `pgadmin` services should show `Up (healthy)` under their status.)_

Absolutely — here's a clean, **important section** you can include in your GitHub README under something like `🔌 Connecting pgAdmin to PostgreSQL in Docker (Windows)`:

---

### 🔌 Connecting pgAdmin to PostgreSQL in Docker (Windows)

If you're using **Docker on Windows** and trying to connect **pgAdmin (in a container)** to your **PostgreSQL database (in another container)**, using `localhost` or `127.0.0.1` as the host **will not work**. That's because each container runs in its own network space.

#### ✅ Use this instead:

```text
Host: host.docker.internal
Port: 5432
Username: <your POSTGRES_USER>      # e.g. mnizhadali
Password: <your POSTGRES_PASSWORD> # e.g. Simpl3P4ssword
Database: <your POSTGRES_DB>       # e.g. hr_training_db
```

`host.docker.internal` is a special DNS name that allows Docker containers to access the host machine, which is where PostgreSQL is actually exposed on port `5432`.

#### Example pgAdmin connection settings:

| Field             | Value                  |
| ----------------- | ---------------------- |
| Name              | `hr_training_db`       |
| Host name/address | `host.docker.internal` |
| Port              | `5432`                 |
| Username          | `mnizhadali`           |
| Password          | `Simpl3P4ssword`       |
| Maintenance DB    | `hr_training_db`       |

1.  **Prepare Python Environment & Run ETL:**
    Set up a Python virtual environment, install necessary libraries, and execute the ETL scripts:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install pandas sqlalchemy psycopg2-binary python-dotenv
    cd etl/
    python3 load_initial_data.py
    python3 transform_data.py
    cd .. # Navigate back to the project root
    ```

    _(This will load your raw CSVs and then transform them into the `fact_training_kpis` table in your PostgreSQL database.)_

2.  **Verify Data (Optional - via pgAdmin on Linux):**
    Open your web browser on Linux and go to `http://localhost:8080`. Log in with your pgAdmin credentials and connect to your PostgreSQL server (`db:5432`) to confirm the tables (especially `fact_training_kpis`) are populated.

3.  **Stop Docker Services on Linux:**
    Once ETL is complete on Linux, it's crucial to stop the containers before transitioning to Windows to avoid port conflicts and ensure data integrity.
    ```bash
    docker-compose down
    ```

### **Phase 2: Setting up the Dashboarding Environment on Windows (Frontend Visualization)** 🖥️

_(Assumes you have Docker Desktop for Windows and Python 3 installed on your Windows OS, with Python added to PATH.)_

1.  **Transfer Project Files:**
    Copy the entire `HR_Training_Dashboard_Project/` folder from your Linux partition to a convenient location on your Windows drive (e.g., `C:\Users\YourUser\Documents\`).

2.  **Launch Docker Desktop for Windows:**
    Ensure Docker Desktop is running in your Windows system tray.

3.  **Restart Database Services on Windows:**
    Open a **new** Command Prompt (CMD) or PowerShell window, navigate to your copied project folder, and restart the Docker services:

    ```cmd
    cd C:\path\to\HR_Training_Dashboard_Project
    docker-compose up -d
    docker-compose ps
    ```

    _(Confirm `Up (healthy)` for both services.)_

4.  **Prepare Python Environment & Re-run ETL (for Windows Database Instance):**
    Although you ran ETL on Linux, it's crucial to re-run it now that a fresh PostgreSQL instance is running on Windows (unless you configured persistent volumes, which is not the default here).

    ```cmd
    python -m venv venv
    .\venv\Scripts\activate
    pip install pandas sqlalchemy psycopg2-binary python-dotenv
    cd etl/
    python load_initial_data.py
    python transform_data.py
    cd ..
    ```

5.  **Verify Data (Recommended - via pgAdmin on Windows):**
    Open your web browser on Windows and go to `http://localhost:8080`. Log in and verify that your `fact_training_kpis` table contains the expected data.

6.  **Install Power BI Desktop:**
    Download and install Power BI Desktop from the official Microsoft website: [https://powerbi.microsoft.com/en-us/downloads/](https://powerbi.microsoft.com/en-us/downloads/).

7.  **Connect Power BI Desktop to PostgreSQL:**
    - Launch Power BI Desktop.
    - Click **"Get Data"** > **"PostgreSQL database"** > "Connect".
    - Enter Connection Details:
      - **Server:** `localhost`
      - **Port:** `5432`
      - **Database:** `your_database_name_e.g._hr_training_db` (from your `.env` file)
    - Click "OK".
    - In the next window, select **"Database"** on the left. Enter your `POSTGRES_USER` and `POSTGRES_PASSWORD`. Click "Connect".
    - In the "Navigator" window, expand your database and the `public` schema.
    - Select the **`fact_training_kpis`** table (and potentially other raw tables if you want them in Power BI for reference) and click **"Load"**.

### **Phase 3: Dashboard Design & Refinement in Power BI** 🎨

1.  **KPI Calculation (DAX Measures):**
    You created several DAX measures for your KPIs:

    - `Total Completed Enrollments`
    - `Total Enrollments`
    - `Course Completion Rate` (formatted as Percentage)
    - `Average Feedback Score` (formatted as Decimal Number)
    - `Active Participant Count`
    - `Total Training Hours Delivered`

2.  **Dashboard Layout & Consolidation:**
    Organize your visuals across a maximum of 1-3 pages for optimal user experience and clarity.

    - **Page 1: "HR Training Overview"**
      - High-level KPI cards at the top.
      - Overall trends (e.g., Active Participants Over Time, Completion Rate Over Time) using line charts.
      - Primary breakdowns (e.g., Completion Rate by Course Category, Average Feedback by Course Category).
      - **Global Slicers:** `Department`, `Course Category`, `Enrollment Year` (or `enrollment_month_year`).
    - **Page 2 (Optional): "Detailed Course Performance"**
      - Focus on individual course names. Bar charts for `Average Feedback Score by Course Name`, `Completion Rate by Course Name`. Maybe a detailed table of course metrics.
    - **Page 3 (Optional): "Department & Participant Insights"**
      - Focus on departmental comparisons. Charts for `Active Participants by Department`, `Completion Rate by Department`, `Training Hours by Department`.

3.  **Refinement & Aesthetics:**
    - Apply a consistent Power BI theme (View tab > Themes).
    - Ensure clear titles for pages and individual visuals.
    - Use consistent font sizes, colors, and visual borders/shadows for a professional look.
    - Validate all interactions (slicers filtering all visuals correctly).

## 🖼️ Dashboard Screenshots

Here are some screenshots of the completed dashboard, showcasing the key insights and interactive elements.

### Overview

![Dashboard Overview Page](/data/images/dashboard_1.png)
_A high-level view of key HR training KPIs and overall trends._

### Course Performance Details

![Course Performance Details Page](/data/images/dashboard_2.png)
_Detailed breakdown of course performance by name and category._

### Departmental Insights

![Departmental Insights Page](/data/images/dashboard_3.png)
_Analysis of training engagement and effectiveness across different departments._

## 🔮 Future Enhancements

- Implement Row-Level Security (RLS) for departmental managers to view only their data.
- Integrate additional HR data sources (e.g., employee demographics, budget data) for richer analysis.
- Automate dashboard refreshes using Power BI Gateway.
- Develop advanced predictive analytics for training needs or success.
- Create drill-through pages for more granular details on specific enrollments or participants.
