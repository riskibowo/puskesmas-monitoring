from flask import Blueprint, jsonify, request
import mysql.connector

pasien_bp = Blueprint("pasien", __name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="puskesmas_monitoring"
    )

@pasien_bp.route("/pasien", methods=["GET"])
def get_all_pasien():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pasien")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(result)

@pasien_bp.route("/pasien/<int:id>", methods=["GET"])
def get_pasien_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pasien WHERE id = %s", (id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return jsonify(result)

@pasien_bp.route("/pasien", methods=["POST"])
def add_pasien():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO pasien (nama, nik, alamat, tanggal_lahir, no_hp) VALUES (%s, %s, %s, %s, %s)"
    val = (data["nama"], data["nik"], data["alamat"], data["tanggal_lahir"], data["no_hp"])
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Pasien berhasil ditambahkan"}), 201

@pasien_bp.route("/pasien/<int:id>", methods=["PUT"])
def update_pasien(id):
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE pasien SET nama=%s, nik=%s, alamat=%s, tanggal_lahir=%s, no_hp=%s WHERE id=%s"
    val = (data["nama"], data["nik"], data["alamat"], data["tanggal_lahir"], data["no_hp"], id)
    cursor.execute(sql, val)
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Pasien berhasil diperbarui"})

@pasien_bp.route("/pasien/<int:id>", methods=["DELETE"])
def delete_pasien(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pasien WHERE id=%s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Pasien berhasil dihapus"})
