import psycopg2
from flask_bcrypt import Bcrypt  # type: ignore
from config import get_db_connection

bcrypt = Bcrypt()

def signup(first_name, last_name, email, password):
   
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM auth WHERE email = %s;', (email,))
    existing_user = cur.fetchone()
    
    if existing_user:
        cur.close()
        conn.close()
        return False 
    
   
    hashed_password = bcrypt.generate_password_hash(password)
    
   
    cur.execute(
        'INSERT INTO auth (first_name, last_name, email, password) VALUES (%s, %s, %s, %s);',
        (first_name, last_name, email, hashed_password)
    )
    conn.commit()

    cur.close()
    conn.close()

    return True
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM auth;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

def signin(email, password):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM auth WHERE email = %s;', (email,))
    user = cur.fetchone()
    
    if user:
        stored_password = user[4] 
        if bcrypt.check_password_hash(stored_password, password):
            return user  
    return None  
