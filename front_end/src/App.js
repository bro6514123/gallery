import React from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";
import MainPage from "./components/Pages/MainPage";
import FormPage from "./components/Pages/FormPage";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainPage />}/>
        <Route path="/form" element={<FormPage />} />
      </Routes>
    </Router>
  )
}

export default App;