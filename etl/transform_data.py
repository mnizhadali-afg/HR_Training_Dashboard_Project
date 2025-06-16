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

# TRANSFORMED_TABLE_NAME = 'transformed_enrollments_participants'
TRANSFORMED_ENROLLMENTS_PARTICIPANTS_TABLE = "transformed_enrollments_participants"
FACT_TABLE_NAME = "fact_training_kpis"

def run_transformation():
    print(f"Connecting to database {DB_NAME} at {DB_HOST}:{DB_PORT}")
    
    try:
        # Create a database engine
        DATABASE_URL = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
        engine = create_engine(DATABASE_URL)
        print("Database engine created successfully.")
        
        # --- First Transformation (Join Enrollments and Participants) ---
        # This part ensures transformed_enrollments_participants is always up-to-date
        # before the final fact table is built.
        print(f"\n--- Building {TRANSFORMED_ENROLLMENTS_PARTICIPANTS_TABLE} ---")

        enroll_part_query = text(f"""
            DROP TABLE IF EXISTS {TRANSFORMED_ENROLLMENTS_PARTICIPANTS_TABLE};

            CREATE TABLE {TRANSFORMED_ENROLLMENTS_PARTICIPANTS_TABLE} AS
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
                enrollments AS e
            JOIN
                participants AS p ON e.participant_id = p.participant_id
        """)
        
        # Execute the transformation query
        with engine.connect() as connection:
            connection.execute(enroll_part_query) # Execute the transformation query
            connection.commit() # Commit the transaction
            print(f"Transformation complete! Table {TRANSFORMED_ENROLLMENTS_PARTICIPANTS_TABLE} created/recreated successfully.")
            
            
        # --- Second Transformation (Create Fact Table: Join with Courses and Feedbacks) ---
        print(f"\n--- Building {FACT_TABLE_NAME} ---")
        fact_table_query = text(f"""
            DROP TABLE IF EXISTS {FACT_TABLE_NAME};
            
            CREATE TABLE {FACT_TABLE_NAME} AS
            SELECT
                tep.enrollment_id,
                tep.participant_id,
                tep.first_name,
                tep.last_name,
                tep.department,
                tep.participant_start_date,
                tep.course_id,
                c.course_name,
                c.category AS course_category,
                c.duration_hours AS training_hours, -- Directly available for 'Training Hours Delivered' KPI
                tep.enrollment_date,
                tep.completion_date,
                tep.score AS enrollment_score, -- Score from enrollment (e.g., quiz score)
                tep.enrollment_status,
                tep.is_completed, -- For 'Course Completion Rate' KPI
                EXTRACT(QUARTER FROM tep.enrollment_date::timestamp) AS enrollment_quarter,
                f.rating AS feedback_score, -- For 'Average Feedback Score' KPI
                f.comments AS feedback_comments,
                -- Derived fields for 'Active Participant Count'
                TO_CHAR(tep.enrollment_date::timestamp, 'YYYY-MM'::text) AS enrollment_month_year,
                TO_CHAR(tep.enrollment_date::timestamp, 'YYYY-Q'::text) AS enrollment_quarter_year
            FROM
                {TRANSFORMED_ENROLLMENTS_PARTICIPANTS_TABLE} AS tep
            LEFT JOIN
                courses AS c ON tep.course_id = c.course_id
            LEFT JOIN
                feedbacks AS f ON tep.enrollment_id = f.enrollment_id
        """)
        
        with engine.connect() as connection:
            connection.execute(fact_table_query)
            connection.commit()
        print(f"Transformation complete! Table {FACT_TABLE_NAME} created/recreated successfully.")
        print("Your data is now ready for dashboarding!")
                
    except Exception as e:
        print(f"An error occurred during the transformation: {e}")
        print(f"Please ensure your database is running and all required raw tables (enrollments, participants, courses, feedbacks) exist.")        
if __name__ == "__main__":
    print("Starting comprehensive data transformation process")
    run_transformation()
    print("Transformation script finished.")