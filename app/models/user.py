import psycopg2
from config import get_db_connection

def create_user(first_name, last_name, email, password):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)',
        (first_name, last_name, email, password)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users
