CREATE DATABASE IF NOT EXISTS puskesmas_monitoring;
USE puskesmas_monitoring;

-- Tabel user untuk login
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

-- Tabel pasien
CREATE TABLE pasien (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    nik VARCHAR(20) UNIQUE NOT NULL,
    alamat TEXT,
    tanggal_lahir DATE,
    no_hp VARCHAR(15)
);

-- Tabel antrian
CREATE TABLE antrian (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pasien_id INT,
    keluhan TEXT,
    tanggal TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (pasien_id) REFERENCES pasien(id) ON DELETE CASCADE
);
