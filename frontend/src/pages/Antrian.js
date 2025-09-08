import React, { useEffect, useState } from "react";
import axios from "axios";
import Navbar from "../components/Navbar";

function Antrian() {
  const [antrian, setAntrian] = useState([]);
  const [newAntrian, setNewAntrian] = useState({ pasien_id: "", keluhan: "" });

  const fetchAntrian = async () => {
    const res = await axios.get("http://127.0.0.1:5000/antrian");
    setAntrian(res.data);
  };

  useEffect(() => {
    fetchAntrian();
  }, []);

  const handleAddAntrian = async (e) => {
    e.preventDefault();
    await axios.post("http://127.0.0.1:5000/antrian", newAntrian);
    setNewAntrian({ pasien_id: "", keluhan: "" });
    fetchAntrian();
  };

  const handleDelete = async (id) => {
    await axios.delete(`http://127.0.0.1:5000/antrian/${id}`);
    fetchAntrian();
  };

  return (
    <div>
      <Navbar />
      <div className="p-6">
        <h1 className="text-2xl font-bold mb-6">Manajemen Antrian</h1>

        <form onSubmit={handleAddAntrian} className="mb-6 bg-white shadow p-4 rounded">
          <input
            type="text"
            placeholder="ID Pasien"
            value={newAntrian.pasien_id}
            onChange={(e) => setNewAntrian({ ...newAntrian, pasien_id: e.target.value })}
            className="border p-2 m-2"
            required
          />
          <input
            type="text"
            placeholder="Keluhan"
            value={newAntrian.keluhan}
            onChange={(e) => setNewAntrian({ ...newAntrian, keluhan: e.target.value })}
            className="border p-2 m-2"
            required
          />
          <button type="submit" className="bg-blue-600 text-white px-4 py-2 rounded">
            Tambah
          </button>
        </form>

        <table className="w-full bg-white shadow rounded">
          <thead>
            <tr className="bg-gray-200 text-left">
              <th className="p-2">ID</th>
              <th className="p-2">ID Pasien</th>
              <th className="p-2">Keluhan</th>
              <th className="p-2">Aksi</th>
            </tr>
          </thead>
          <tbody>
            {antrian.map((a) => (
              <tr key={a.id}>
                <td className="p-2">{a.id}</td>
                <td className="p-2">{a.pasien_id}</td>
                <td className="p-2">{a.keluhan}</td>
                <td className="p-2">
                  <button
                    onClick={() => handleDelete(a.id)}
                    className="bg-red-500 text-white px-2 py-1 rounded"
                  >
                    Hapus
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Antrian;
