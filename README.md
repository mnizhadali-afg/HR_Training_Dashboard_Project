# HR Training Dashboard Project

[![Python](https://img.shields.io/badge/Python-3.12.6-blue.svg)](https://www.python.org/)
[![Automation](https://img.shields.io/badge/Automation-GitHub_Actions-yellow.svg)](https://github.com/features/actions)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Project Overview

This project focuses on building a comprehensive HR Training Dashboard using a modern data stack. It involves setting up a robust data pipeline to extract raw training data, transform it into a clean, analytical format, and then visualize key performance indicators (KPIs) in Power BI to provide actionable insights into training effectiveness and participant engagement.

The project demonstrates skills in Docker for containerization, PostgreSQL for database management, Python for ETL (Extract, Transform, Load) processes, and Power BI for interactive data visualization.

## Goal

Simulate improving and automating a hypothetical internal process (e.g., tracking training completion, feedback, or participant engagement) and visualize its performance. This project directly touches upon data integration, automation, visualization, and process thinking, with a strong link to your lecturing background.

## Scenario

Imagine a company has a global training department (like the one in the "Education Expert IT" role). They manually track course completion, participant feedback, and engagement across various platforms (some old, some new). Your task is to automate this, centralize the data, and provide insights.

## Key Features

- **Automated Data Ingestion:** Scripts to load raw training data from CSV files into a PostgreSQL database.
- **Data Transformation:** Python-based ETL process to clean, enrich, and transform raw data into a star-schema-like structure, culminating in a `fact_training_kpis` table ready for analysis.
- **Database Management:** Containerized PostgreSQL for efficient and isolated data storage, with pgAdmin for database administration.
- **Key Performance Indicators (KPIs):** Calculation and visualization of critical HR training metrics, including:
  - **Course Completion Rate:** Percentage of completed training enrollments.
  - **Average Course Feedback Score:** Participant satisfaction with training programs.
  - **Active Participant Count:** Number of unique individuals engaging in training over time.
  - **Total Training Hours Delivered:** Overall investment in training programs.
- **Interactive Dashboard:** A Power BI dashboard enabling drill-down analysis by course category, department, time, and more.
- **Dual-OS Setup Compatibility:** Instructions for setting up the data pipeline on Linux and seamlessly transitioning to Windows for dashboarding.

## Technologies Used

- **Operating Systems:** Linux (e.g., Ubuntu), Windows
- **Containerization:** Docker, Docker Compose
- **Database:** PostgreSQL
- **Database Management:** pgAdmin
- **Programming Language:** Python 3
- **Python Libraries:** `pandas`, `sqlalchemy`, `psycopg2-binary`, `python-dotenv`
- **Business Intelligence:** Microsoft Power BI Desktop
- **Version Control:** Git, GitHub

## Project Structure

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
├── etl/
│   └── load_initial_data.py     # Script to load initial raw CSVs into PostgreSQL
│   └── transform_data.py        # Script to load all required KPIs into a Fact Table in PostgreSQL
├── venv/                        # Python virtual environment
├── .env                         # Environment variables for sensitive data (e.g., DB credentials)
├── .gitignore                   # Specifies files/directories to ignore in Git
├── docker-compose.yml           # Defines Docker services (PostgreSQL, pgAdmin)
└── README.md                    # Project documentation
```

## Initial Data Sources

- `data/raw/participants.csv`: Contains participant demographic information.
- `data/raw/courses.csv`: Contains details about training courses.
- `data/raw/enrollments.csv`: Records participant enrollments, completion status, and scores.
- `data/raw/feedbacks.csv`: Stores feedback ratings and comments for enrollments.
- `data/raw/engagements.csv`: Contains engagement data (initially as a flat file, later served via API).
- **API Endpoint (`api/api.py`):** Serves `engagements` data in JSON format.
  - Base URL: `http://127.0.0.1:5000/`
  - Engagements Endpoint: `http://127.0.0.1:5000/api/engagements`
  - To run the API: Navigate to the `api/` directory (after activating virtual environment) and execute `python api.py`.

### Initial Data Schema

![Initial Data Schema](/data/images/schema.png)

## Setup Instructions

**1. Prerequisites:**

- Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running on your system.

**2. Configuration (Environment Variables):**

- Sensitive credentials (PostgreSQL username/password/DB name, pgAdmin login) are managed using environment variables loaded from a `.env` file.
- Create a file named `.env` in the **root of the project directory** (next to `docker-compose.yml`).
- Add the following variables, replacing placeholders with your actual secure values:
  ```
  POSTGRES_USER=your_db_username
  POSTGRES_PASSWORD=your_db_password
  POSTGRES_DB=your_database_name
  PGADMIN_DEFAULT_EMAIL=your_pgadmin_email@example.com
  PGADMIN_DEFAULT_PASSWORD=your_pgadmin_password
  PGADMIN_LISTEN_PORT=8080 # Host port for pgAdmin
  DB_PORT=5432             # Host port for PostgreSQL
  ```
- **Security Note:** Ensure `.env` is listed in your `.gitignore` file (`.gitignore` should contain `/`.env`) to prevent it from being committed to your public repository.

**3. Starting the Database Services:**

- Open your terminal and navigate to the project root directory (`HR_Training_Dashboard_Project/`).
- Start the PostgreSQL database and pgAdmin containers in detached mode (background):
  ```bash
  docker-compose up -d
  ```
- To check the status of your containers:
  ```bash
  docker-compose ps
  ```
  (Ensure `db` shows `Up (healthy)` and `pgadmin` shows `Up`).
- To stop and remove the containers (and their associated persistent data volumes for a clean slate, use with caution in development):
  ```bash
  docker-compose down -v
  ```

**4. Accessing pgAdmin (Database GUI):**

- Once the Docker containers are running, open your web browser.
- Navigate to: `http://localhost:8080`
- Log in using the `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD` defined in your `.env` file.

**5. Registering PostgreSQL Server in pgAdmin:**

- Inside the pgAdmin web interface, right-click on "Servers" in the left panel and select "Register" > "Server...".
- **General Tab:**
  - **Name:** `HR Training Database` (or any descriptive name).
- **Connection Tab:**
  - **Host name/address:** `db` (This is the Docker Compose service name for the PostgreSQL container, enabling internal communication within the Docker network).
  - **Port:** `5432`
  - **Maintenance database:** `${POSTGRES_DB}` (e.g., `hr_training_db` from your `.env` file).
  - **Username:** `${POSTGRES_USER}` (e.g., `your_db_username` from your `.env` file).
  - **Password:** `${POSTGRES_PASSWORD}` (e.g., `your_db_password` from your `.env` file).
- Click "Save". You should now see your database listed and be able to explore its schemas and tables.

## Data Loading

Initial raw data from CSV files is loaded into the PostgreSQL database using a Python script.

**1. Install Python Dependencies:**

- Ensure your Python virtual environment is activated.
- Install necessary libraries:
  ```bash
  pip install SQLAlchemy psycopg2-binary
  ```

**2. Load All Raw CSVs:**

- The script `etl/load_initial_data.py` is designed to read all raw CSV files from `data/raw/` and load them into corresponding tables in your PostgreSQL database.
- Navigate to the `etl/` directory in your terminal:
  ```bash
  cd etl/
  ```
- Run the script:
  ```bash
  python load_initial_data.py
  ```
- **Verification:** After running the script, verify in pgAdmin (`http://localhost:8080`) under your `HR Training Database` > `Databases` > `your_database_name` > `Schemas` > `public` > `Tables`. You should see the following tables populated with data:
  - `participants`
  - `courses`
  - `enrollments`
  - `feedbacks`
  - `engagements`

## Data Transformation

The project employs Python scripts to transform raw data from the initial CSV imports into a clean, unified, and analytical-ready format suitable for dashboarding and KPI calculations.

### Transformation Script: `etl/transform_data.py`

This script orchestrates the core data transformation steps:

1.  **Initial Join (`transformed_enrollments_participants`):** It first performs a join between the `enrollments` and `participants` tables. This step integrates participant demographics with their enrollment records and derives basic fields like `is_completed`, `enrollment_year`, and `enrollment_month`. This intermediate result is stored in the `transformed_enrollments_participants` table.
2.  **Fact Table Creation (`fact_training_kpis`):** Building upon the previous step, this script then creates a comprehensive "fact" table named `fact_training_kpis`. This is achieved by:
    - **Joining** `transformed_enrollments_participants` with `courses` to add course details (e.g., `course_name`, `training_hours`).
    - **Joining** with `feedbacks` to incorporate feedback scores and comments.
    - The `fact_training_kpis` table serves as the primary data source for dashboarding, containing all necessary fields to directly calculate KPIs like Course Completion Rate, Average Course Feedback Score, Active Participant Count, and Training Hours Delivered. It includes aggregated and derived fields ready for visualization.

## Dashboarding Setup (On Windows)

1.  **Transfer Project to Windows:**
    Copy the entire `HR_Training_Dashboard_Project/` folder from your Linux partition to a suitable location on your Windows drive (e.g., `C:\Users\YourUser\Documents\`).

2.  **Install Docker Desktop for Windows:**
    Download and install Docker Desktop from [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/). Ensure it's running after installation.

3.  **Start Docker Services on Windows:**
    Open Command Prompt (CMD) or PowerShell on Windows, navigate to your copied `HR_Training_Dashboard_Project/` folder, and start the services:

    ```cmd
    cd C:\path\to\HR_Training_Dashboard_Project
    docker-compose up -d
    docker-compose ps
    ```

    (Confirm `Up (healthy)` status for both services.)

4.  **Install Python on Windows & Re-run ETL (Crucial for Windows Database)**:

    - If Python isn't installed, download the installer from [python.org/downloads/windows/](https://www.python.org/downloads/windows/). **Crucially, check "Add python.exe to PATH" during installation.**
    - Open a **new** Command Prompt/PowerShell.
    - Navigate to your project root: `cd C:\path\to\HR_Training_Dashboard_Project`
    - Set up Python environment:
      ```cmd
      python -m venv venv
      .\venv\Scripts\activate
      pip install pandas sqlalchemy psycopg2-binary python-dotenv
      ```
    - Navigate to `etl/` and re-run scripts to populate the database now running on Windows:
      ```cmd
      cd etl/
      python load_initial_data.py
      python transform_data.py
      cd ..
      ```
    - **Verify Data in pgAdmin (Optional but Recommended):** Access `http://localhost:8080`, log in, and verify that the `fact_training_kpis` table in your `public` schema contains data.

5.  **Install Power BI Desktop:**
    Download and install Power BI Desktop from the official Microsoft Power BI website: [powerbi.microsoft.com/en-us/downloads/](https://powerbi.microsoft.com/en-us/downloads/).

6.  **Connect Power BI Desktop to PostgreSQL:**
    - Open Power BI Desktop.
    - Click **"Get Data"** > **"PostgreSQL database"** > "Connect".
    - **Server:** `localhost`
    - **Database:** `your_database_name` (from your `.env` file)
    - Click "OK".
    - Select **"Database"** on the left, enter your `POSTGRES_USER` and `POSTGRES_PASSWORD`. Click "Connect".
    - In the "Navigator" window, expand your database and `public` schema.
    - Select the **`fact_training_kpis`** table and click **"Load"**.

## Dashboard Overview

The Power BI dashboard provides key insights into HR training performance. It is organized into several pages (recommended: 1-3 pages) for clarity and ease of navigation.

**Key Dashboard Pages (Suggested):**

- **Training Overview:** High-level KPIs (Completion Rate, Avg. Feedback, Active Participants, Total Hours), with overall trends.
- **Course Performance:** Detailed analysis of specific courses, categories, and their associated completion rates and feedback scores.
- **Participant & Department Analysis:** Insights into participant engagement and training performance across different departments.

## Future Enhancements (Ideas for continued development)

- Add more detailed participant demographics (e.g., age, tenure).
- Incorporate training cost data for ROI analysis.
- Implement row-level security for departmental managers.
- Create drill-through pages for detailed enrollment specifics.
- Automate Power BI dashboard refresh using a Power BI Gateway.
- Integrate with other HR systems.

---
