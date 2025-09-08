import React from "react";
import { Link, useNavigate } from "react-router-dom";

function Navbar() {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/login");
  };

  return (
    <nav className="bg-gray-800 p-4 text-white flex justify-between items-center">
      <div className="flex space-x-4">
        <Link to="/dashboard" className="hover:text-gray-300 font-semibold">Dashboard</Link>
        <Link to="/pasien" className="hover:text-gray-300 font-semibold">Pasien</Link>
        <Link to="/antrian" className="hover:text-gray-300 font-semibold">Antrian</Link>
      </div>
      <button
        onClick={handleLogout}
        className="bg-red-500 hover:bg-red-600 px-3 py-1 rounded"
      >
        Logout
      </button>
    </nav>
  );
}

export default Navbar;
