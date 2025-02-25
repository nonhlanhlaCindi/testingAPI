import psycopg2
from flask_bcrypt import Bcrypt  # type: ignore
from config import get_db_connection

bcrypt = Bcrypt()

def signup(first_name, last_name, email, password):
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO auth (first_name, last_name, email, password) VALUES (%s, %s, %s, %s);',
        (first_name, last_name, email, hashed_password)
    ) 
    conn.commit()
    if cur.rowcount == 1:
        result = True
    else:
        result = False
    
    cur.close()
    conn.close()
    
    return result

def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM auth;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users
