import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ------ Configuration ------
DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_NAME = os.getenv('POSTGRES_DB')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('DB_PORT', '5432')

TRANSFORMED_TABLE_NAME = 'transformed_enrollments_participants'

def run_transformation():
    print(f"Connecting to database {DB_NAME} at {DB_HOST}:{DB_PORT}")
    
    try:
        # Create a database engine
        DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        engine = create_engine(DATABASE_URL)
        print("Database engine created successfully.")
        
        # SQL query to join enrollments and participants tables
        # The 1st. transformation
        transformation_query = text(f"""
            DROP TABLE IF EXISTS {TRANSFORMED_TABLE_NAME};

            CREATE TABLE {TRANSFORMED_TABLE_NAME} AS
            SELECT
                e.enrollment_id,
                e.participant_id,
                p.first_name,
                p.last_name,
                p.department,
                p.start_date_at_company AS participant_start_date,
                e.course_id,
                e.enrollment_date,
                e.completion_date,
                e.score,
                e.status as enrollment_status,
                CASE
                    WHEN e.status = 'completed' THEN TRUE
                    ELSE FALSE
                END AS is_completed,
                EXTRACT(YEAR FROM e.enrollment_date::timestamp) AS enrollment_year,
                EXTRACT(MONTH FROM e.enrollment_date::timestamp) AS enrollment_month
            FROM
                enrollments e
            JOIN
                participants AS p ON e.participant_id = p.participant_id
        """)
        
        # Execute the transformation query
        with engine.connect() as connection:
            connection.execute(transformation_query) # Execute the transformation query
            connection.commit() # Commit the transaction
        
        print(f"Transformation complete! Table {TRANSFORMED_TABLE_NAME} created/recreated successfully.")
        
    except Exception as e:
        print(f"An error occurred during the transformation: {e}")
        print(f"Please check your database connection and query syntax.")
        
if __name__ == "__main__":
    print("Starting data transformation...")
    run_transformation()
    print("Data transformation completed.")