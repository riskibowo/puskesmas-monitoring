import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",        # sesuaikan
        password="",        # sesuaikan
        database="puskesmas_db"
    )
    return conn
