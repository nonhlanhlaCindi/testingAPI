import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="users",
        user="postgres", 
        password="my_password",  
        host="localhost",
        port="5432"
    )
    return conn