import { Routes, Route } from "react-router-dom"
import React, { useState } from "react";
import "./App.css";
// Models
import { Todo } from "./models/models";

// Pages Imports
import HomePage from "./pages/HomePage/HomePage";
import LoginPage from "./pages/LoginPage/LoginPage";
import RegisterPage from "./pages/RegisterPage/RegisterPage";


// Components
import NavBar from "./components/NavBar/NavBar";
import Footer from "./components/Footer/Footer";

// Util Imports
import PrivateRoute from "./utils/PrivateRoute";


const App: React.FC = () => {
  
  return (
    <div className="container">
    <NavBar />
    <Routes>
      <Route
        path="/"
        element={
          <PrivateRoute>
            <HomePage />
          </PrivateRoute>
        }
        />
        
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />

      </Routes>
      <Footer />
    </div>
  );
};

export default App;