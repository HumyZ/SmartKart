import './App.css';
import Home from "./components/Home";
import Login from "./components/Login";
import Signup from './components/Signup';
import Items from "./components/Items";
import Cart from "./components/Cart";
import Subcategory from './components/Subcategory';
import {HashRouter as Router, Route, Routes} from "react-router-dom";
import React from 'react'
import ReactDOM from 'react-dom'
import PickUp from './components/PickUp';

function App() {
  return (
    <Router>
    <div className="App">
      <Routes>
      <Route path= "/" element={<Home/>}/>
      <Route path="/items" element={<Items/>}/>
      <Route path="/login" element={<Login/>}/>
      <Route path="/signup" element={<Signup/>}/>
      <Route path="/subcategory" element={<Subcategory/>}/>
      <Route path="/pickup" element={<PickUp/>}/>
      <Route path="/cart" element={<Cart/>}/>

      </Routes>
    </div>
    </Router>
      
  );
}

export default App;
