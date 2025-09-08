import React, { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

function Pasien() {
  const [pasien, setPasien] = useState([]);

  const fetchPasien = async () => {
    const res = await axios.get("http://127.0.0.1:5000/pasien");
    setPasien(res.data);
  };

  useEffect(() => {
    fetchPasien();
  }, []);

  return (
    <div>
      <Navbar />
      <div className="p-6">
        <h1 className="text-2xl font-bold mb-4">Data Pasien</h1>
        <table className="w-full border">
          <thead>
            <tr>
              <th className="border p-2">ID</th>
              <th className="border p-2">Nama</th>
              <th className="border p-2">NIK</th>
              <th className="border p-2">Alamat</th>
              <th className="border p-2">Tanggal Lahir</th>
              <th className="border p-2">No HP</th>
            </tr>
          </thead>
          <tbody>
            {pasien.map((p) => (
              <tr key={p.id}>
                <td className="border p-2">{p.id}</td>
                <td className="border p-2">{p.nama}</td>
                <td className="border p-2">{p.nik}</td>
                <td className="border p-2">{p.alamat}</td>
                <td className="border p-2">{p.tanggal_lahir}</td>
                <td className="border p-2">{p.no_hp}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Pasien;
