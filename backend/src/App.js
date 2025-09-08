import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Pasien from "./pages/Pasien";
import Antrian from "./pages/Antrian";

function App() {
  return (
    <Router>
      <div className="p-6">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/pasien" element={<Pasien />} />
          <Route path="/antrian" element={<Antrian />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
