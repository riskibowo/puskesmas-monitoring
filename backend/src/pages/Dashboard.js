import React, { useEffect, useState } from "react";

function Dashboard() {
  const [data, setData] = useState({ pasien: 0, antrian: 0 });

  useEffect(() => {
    const fetchData = async () => {
      const res = await fetch("http://127.0.0.1:5000/dashboard");
      const json = await res.json();
      setData(json);
    };
    fetchData();
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">Dashboard</h1>
      <div className="grid grid-cols-2 gap-4">
        <div className="bg-white shadow rounded p-4">
          <h2 className="font-semibold">Total Pasien</h2>
          <p className="text-xl">{data.pasien}</p>
        </div>
        <div className="bg-white shadow rounded p-4">
          <h2 className="font-semibold">Total Antrian Hari Ini</h2>
          <p className="text-xl">{data.antrian}</p>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
