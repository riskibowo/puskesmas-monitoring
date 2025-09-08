from flask import Blueprint, jsonify, request
import mysql.connector
from datetime import datetime

antrian_bp = Blueprint("antrian", __name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="puskesmas_monitoring"
    )

@antrian_bp.route("/antrian", methods=["GET"])
def get_all_antrian():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM antrian")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)

@antrian_bp.route("/antrian", methods=["POST"])
def add_antrian():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO antrian (pasien_id, keluhan, tanggal) VALUES (%s, %s, %s)"
    val = (data["pasien_id"], data["keluhan"], datetime.now())
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Antrian berhasil ditambahkan"}), 201

@antrian_bp.route("/antrian/<int:id>", methods=["DELETE"])
def delete_antrian(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM antrian WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Antrian berhasil dihapus"})
