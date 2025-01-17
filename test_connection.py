import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try:

    connection = psycopg2.connect(
        user=os.getenv("USER"),
        password=os.getenv("PASSWORD"),
        host=os.getenv("HOST"),
        port=os.getenv("PORT"),
        database=os.getenv("DATABASE")
    )

    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    
    # Close the cursor and connection
    cursor.close()
    connection.close()

except Exception as e:
    print(f"Error: {e}")