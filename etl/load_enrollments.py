import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ----- Configuration -----
# Database connection from .env file
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('POSTGRES_DB')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('DB_PORT')  # Default PostgreSQL port

# Path to enrollments.csv
ENROLLMENTS_CSV_PATH = os.path.join('..', 'data', 'raw', 'enrollments.csv')

# Create a Table in the database
TABLE_NAME = 'enrollments'

def load_enrollments_data():
    print(f"Attempting to load enrollments data from CSV...")
    print(f"Connecting to the database: {DB_NAME} at {DB_HOST}:{DB_PORT}")
    
    try:
        # 1. Read the CSV file into a DataFrame
        df = pd.read_csv(ENROLLMENTS_CSV_PATH)
        print(f"Seccessfully loaded {len(df)} rows from {ENROLLMENTS_CSV_PATH}")
        
        # 2. Establish a database connection
        DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        engine = create_engine(DATABASE_URL)
        print("Database connection established successfully.")
        
        # 3. Load the DataFrame into the database
        df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False)
        print(f"Data loaded successfully into the table '{TABLE_NAME}'.")
        
    except FileNotFoundError:
        print(f"Error: The file {ENROLLMENTS_CSV_PATH} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your database connection settings and the CSV file path.")
        
if __name__ == "__main__":
    print("Make sure your Dockerized PostgreSQL database is running (docker-compose up -d).")
    load_enrollments_data()