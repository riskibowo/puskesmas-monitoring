import React from "react";
import Navbar from "../components/Navbar";

function Dashboard() {
  return (
    <div>
      <Navbar />
      <div className="p-6">
        <h1 className="text-2xl font-bold mb-4">Dashboard</h1>
        <p>Selamat datang di sistem monitoring Puskesmas!</p>
      </div>
    </div>
  );
}

export default Dashboard;
