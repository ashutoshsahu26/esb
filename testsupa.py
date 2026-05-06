import psycopg2
from psycopg2 import extras

# Replace with your actual connection string from Supabase
DB_URL = "postgresql://postgres:PBcUcjswd8jxRXKD@db.fflnyzlxlulppfrlsgfe.supabase.co:5432/postgres"

def fetch_data_direct():
    conn = None
    try:
        # 1. Connect to the Postgres database
        conn = psycopg2.connect(DB_URL)
        
        # 2. Create a cursor (RealDictCursor returns rows as Python dictionaries)
        cur = conn.cursor(cursor_factory=extras.RealDictCursor)
        
        # 3. Execute a standard SQL query
        query = "SELECT * FROM test;"
        cur.execute(query)
        
        # 4. Fetch the results
        rows = cur.fetchall()
        
        for row in rows:
            # Access columns by name: row['username']
            print(row)
            
    except Exception as e:
        print(f"Database error: {e}")
        
    finally:
        # 5. Always close the connection!
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection closed.")

if __name__ == "__main__":
    fetch_data_direct()