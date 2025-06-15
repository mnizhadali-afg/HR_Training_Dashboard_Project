import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = "localhost"
DB_PORT = os.getenv("DB_PORT") # Should be 5432

# Base path to your raw data directory
RAW_DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'raw')

# List of (CSV filename, table name) pairs to load
# Ensure these CSVs exist in your data/raw directory
FILES_TO_LOAD = [
    ("participants.csv", "participants"),
    ("courses.csv", "courses"),
    ("enrollments.csv", "enrollments"),
    ("feedbacks.csv", "feedbacks"),
    ("engagements.csv", "engagements"),
]

def load_csv_to_db(csv_filename, table_name, engine):
    """
    Loads a CSV file into a specified PostgreSQL table.
    """
    csv_file_path = os.path.join(RAW_DATA_DIR, csv_filename)
    print(f"\n--- Loading {csv_filename} into table '{table_name}' ---")

    try:
        df = pd.read_csv(csv_file_path)
        print(f"Successfully loaded {len(df)} rows from {csv_filename}")

        # Load DataFrame into PostgreSQL table
        # if_exists='replace': Replaces the table if it already exists (useful for development)
        # index=False: Prevents Pandas from writing the DataFrame index as a column
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data successfully loaded into table '{table_name}' in PostgreSQL.")

    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_file_path}. Skipping this file.")
    except Exception as e:
        print(f"An error occurred while loading {csv_filename}: {e}")

if __name__ == "__main__":
    print("Starting data loading process...")

    try:
        # Create a database engine once
        DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        engine = create_engine(DATABASE_URL)
        print("Database engine created and connection pool initialized.")

        # Test connection (optional, but good for early error detection)
        with engine.connect() as connection:
            print(f"Successfully connected to PostgreSQL database: {DB_NAME}")

        # Iterate through the list of files and load each one
        for csv_file, table in FILES_TO_LOAD:
            load_csv_to_db(csv_file, table, engine)

        print("\nAll specified CSV files processed.")

    except Exception as e:
        print(f"\nCritical error during database connection or overall loading process: {e}")
        print("Please ensure your Dockerized PostgreSQL DB is running (docker-compose up -d) and credentials are correct.")