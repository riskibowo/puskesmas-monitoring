from flask import Blueprint, jsonify
import mysql.connector

dashboard_bp = Blueprint("dashboard", __name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="puskesmas_monitoring"
    )

@dashboard_bp.route("/dashboard", methods=["GET"])
def get_dashboard():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) as total_pasien FROM pasien")
    total_pasien = cursor.fetchone()["total_pasien"]

    cursor.execute("SELECT COUNT(*) as total_antrian FROM antrian")
    total_antrian = cursor.fetchone()["total_antrian"]

    cursor.close()
    conn.close()

    return jsonify({
        "total_pasien": total_pasien,
        "total_antrian": total_antrian
    })
