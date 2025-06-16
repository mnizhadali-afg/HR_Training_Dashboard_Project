# HR Training Dashboard Project

[![Python](https://img.shields.io/badge/Python-3.12.6-blue.svg)](https://www.python.org/)
[![Automation](https://img.shields.io/badge/Automation-GitHub_Actions-yellow.svg)](https://github.com/features/actions)
[![Status](https://img.shields.io/badge/Status-Active-green.svg)](https://github.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Project Overview
This project aims to build an automated data pipeline and dashboard to visualize key performance indicators (KPIs) for internal HR/Training programs. It involves integrating data from various simulated sources, transforming it, and presenting it through an interactive dashboard.

## Goal
Simulate improving and automating a hypothetical internal process (e.g., tracking training completion, feedback, or participant engagement) and visualize its performance. This project directly touches upon data integration, automation, visualization, and process thinking, with a strong link to your lecturing background.

## Scenario
Imagine a company has a global training department (like the one in the "Education Expert IT" role). They manually track course completion, participant feedback, and engagement across various platforms (some old, some new). Your task is to automate this, centralize the data, and provide insights.

## Key Performance Indicators (KPIs)
1.  **Course Completion Rate:** (Percentage of enrolled users who completed a course)
2.  **Average Course Feedback Score**: (Overall satisfaction with courses)
3.  **Active Participant Count:** (Number of unique users engaging with training each month/quarter)
4.  **Training Hours Delivered:** (Total hours of training provided)

## Technologies Used
* **Python** (for data generation, ETL, and API)
    * Libraries: `pandas`, `Flask`, `csv`, **`SQLAlchemy`**, **`psycopg2-binary`**
* **PostgreSQL** (for relational database)
* **Docker** & **Docker Compose** (for containerizing PostgreSQL and pgAdmin)
* **pgAdmin** (GUI for interacting with PostgreSQL database)
* **Tableau Public / Power BI Desktop** (for dashboarding - to be used in Week 2)
* **Git & GitHub** (for version control)
* **JSON** (data format for API)

## Initial Data Sources
* `data/raw/participants.csv`: Contains participant demographic information.
* `data/raw/courses.csv`: Contains details about training courses.
* `data/raw/enrollments.csv`: Records participant enrollments, completion status, and scores.
* `data/raw/feedbacks.csv`: Stores feedback ratings and comments for enrollments.
* `data/raw/engagements.csv`: Contains engagement data (initially as a flat file, later served via API).
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
│   ├── raw/                     # Contains raw CSV data files
│   │   ├── participants.csv
│   │   ├── courses.csv
│   │   ├── enrollments.csv
│   │   ├── feedbacks.csv
│   │   └── engagements.csv
│   └── images/
│       └── schema.png           # Database schema diagram
├── etl/
│   └── load_initial_data.py     # Script to load all raw CSVs into PostgreSQL
├── venv/                        # Python virtual environment
├── .env                         # Environment variables for sensitive data (e.g., DB credentials)
├── .gitignore                   # Specifies files/directories to ignore in Git
├── docker-compose.yml           # Defines Docker services (PostgreSQL, pgAdmin)
└── README.md                    # Project documentation
```

## Database Setup (PostgreSQL with Docker Compose)

The project leverages a PostgreSQL database and pgAdmin (a GUI for database management) running in Docker containers, orchestrated by Docker Compose. This ensures a consistent and isolated development environment.

### Initial Data Schema
![Initial Data Schema](/data/images/schema.png)

**1. Prerequisites:**
* Ensure you have [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running on your system.



**2. Configuration (Environment Variables):**
* Sensitive credentials (PostgreSQL username/password/DB name, pgAdmin login) are managed using environment variables loaded from a `.env` file.
* Create a file named `.env` in the **root of the project directory** (next to `docker-compose.yml`).
* Add the following variables, replacing placeholders with your actual secure values:
    ```
    POSTGRES_USER=your_db_username
    POSTGRES_PASSWORD=your_db_password
    POSTGRES_DB=your_database_name
    PGADMIN_DEFAULT_EMAIL=your_pgadmin_email@example.com
    PGADMIN_DEFAULT_PASSWORD=your_pgadmin_password
    PGADMIN_LISTEN_PORT=8080 # Host port for pgAdmin
    DB_PORT=5432             # Host port for PostgreSQL
    ```
* **Security Note:** Ensure `.env` is listed in your `.gitignore` file (`.gitignore` should contain `/`.env`) to prevent it from being committed to your public repository.

**3. Starting the Database Services:**
* Open your terminal and navigate to the project root directory (`HR_Training_Dashboard_Project/`).
* Start the PostgreSQL database and pgAdmin containers in detached mode (background):
    ```bash
    docker-compose up -d
    ```
* To check the status of your containers:
    ```bash
    docker-compose ps
    ```
    (Ensure `db` shows `Up (healthy)` and `pgadmin` shows `Up`).
* To stop and remove the containers (and their associated persistent data volumes for a clean slate, use with caution in development):
    ```bash
    docker-compose down -v
    ```

**4. Accessing pgAdmin (Database GUI):**
* Once the Docker containers are running, open your web browser.
* Navigate to: `http://localhost:8080`
* Log in using the `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD` defined in your `.env` file.

**5. Registering PostgreSQL Server in pgAdmin:**
* Inside the pgAdmin web interface, right-click on "Servers" in the left panel and select "Register" > "Server...".
* **General Tab:**
    * **Name:** `HR Training Database` (or any descriptive name).
* **Connection Tab:**
    * **Host name/address:** `db` (This is the Docker Compose service name for the PostgreSQL container, enabling internal communication within the Docker network).
    * **Port:** `5432`
    * **Maintenance database:** `${POSTGRES_DB}` (e.g., `hr_training_db` from your `.env` file).
    * **Username:** `${POSTGRES_USER}` (e.g., `your_db_username` from your `.env` file).
    * **Password:** `${POSTGRES_PASSWORD}` (e.g., `your_db_password` from your `.env` file).
* Click "Save". You should now see your database listed and be able to explore its schemas and tables.

## Data Loading

Initial raw data from CSV files is loaded into the PostgreSQL database using a Python script.

**1. Install Python Dependencies:**
* Ensure your Python virtual environment is activated.
* Install necessary libraries:
    ```bash
    pip install SQLAlchemy psycopg2-binary
    ```

**2. Load All Raw CSVs:**
* The script `etl/load_initial_data.py` is designed to read all raw CSV files from `data/raw/` and load them into corresponding tables in your PostgreSQL database.
* Navigate to the `etl/` directory in your terminal:
    ```bash
    cd etl/
    ```
* Run the script:
    ```bash
    python load_initial_data.py
    ```
* **Verification:** After running the script, verify in pgAdmin (`http://localhost:8080`) under your `HR Training Database` > `Databases` > `your_database_name` > `Schemas` > `public` > `Tables`. You should see the following tables populated with data:
    * `participants`
    * `courses`
    * `enrollments`
    * `feedbacks`
    * `engagements`

## Data Transformation

The project employs Python scripts to transform raw data into a clean, unified format suitable for analysis and dashboarding.

### First Transformation: `etl/transform_data.py`

This script performs the initial data transformation by:
* **Joining** the `enrollments` table with the `participants` table.
* **Creating new derived fields** such as `is_completed` (a boolean flag based on enrollment status), `enrollment_year`, and `enrollment_month` from the `enrollment_date`.
* The resulting transformed data is saved into a new table named `transformed_enrollments_participants` in the PostgreSQL database.
