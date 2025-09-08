# 1. Tabel pasien

# Menyimpan data pasien.

# CREATE TABLE pasien (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nama VARCHAR(100) NOT NULL,
#     nik VARCHAR(20) UNIQUE NOT NULL,
#     alamat TEXT,
#     tanggal_lahir DATE,
#     no_hp VARCHAR(15),
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# 📌 2. Tabel dokter

# Menyimpan data dokter.

# CREATE TABLE dokter (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nama VARCHAR(100) NOT NULL,
#     spesialis VARCHAR(100),
#     no_hp VARCHAR(15),
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );

# 📌 3. Tabel antrian

# Menyimpan data antrian pasien tiap hari.

# CREATE TABLE antrian (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     pasien_id INT NOT NULL,
#     dokter_id INT NOT NULL,
#     nomor_antrian INT NOT NULL,
#     tanggal DATE NOT NULL,
#     status ENUM('menunggu', 'dipanggil', 'selesai') DEFAULT 'menunggu',
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (pasien_id) REFERENCES pasien(id) ON DELETE CASCADE,
#     FOREIGN KEY (dokter_id) REFERENCES dokter(id) ON DELETE CASCADE
# );

# 📌 4. Tabel kunjungan

# Menyimpan riwayat kunjungan pasien ke puskesmas.

# CREATE TABLE kunjungan (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     pasien_id INT NOT NULL,
#     dokter_id INT NOT NULL,
#     keluhan TEXT,
#     diagnosa TEXT,
#     resep_obat TEXT,
#     tanggal DATE NOT NULL,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     FOREIGN KEY (pasien_id) REFERENCES pasien(id) ON DELETE CASCADE,
#     FOREIGN KEY (dokter_id) REFERENCES dokter(id) ON DELETE CASCADE
# );

# 📌 5. Tabel users (opsional → untuk login admin/petugas)

# Kalau nanti mau ada login/logout.

# CREATE TABLE users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     username VARCHAR(50) UNIQUE NOT NULL,
#     password VARCHAR(255) NOT NULL, -- simpan hash, jangan plain text
#     role ENUM('admin', 'petugas') DEFAULT 'petugas',
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# );


# ⚡ Dengan model ini:

# Dashboard bisa menampilkan total pasien, total antrian hari ini, jumlah dokter, dll.

# CRUD Pasien → dari tabel pasien.

# Antrian → nomor antrian auto di-generate berdasarkan pasien + tanggal.

# Kunjungan → menyimpan catatan medis pasien.