import React from 'react'
import {useNavigate} from 'react-router-dom';
import {Link} from 'react-router-dom'
import Nav from "./Nav";
import walking from './images/walking.png';
import bicycle from './images/bicycle.png';
import car from './images/car.png';
import {useState, useEffect} from 'react';




{/* responsible for pickup page */}
function PickUp() {
  const [method, setMethod] = useState('');



  {/* Waits for setCategory to set category state before calling the handleSubmit function */}
  useEffect(() => {
    handleSubmit();
}, [method])


function handleSubmit(e){
 
  
}
  return (
    <div>
      <Nav />
      <h1> How do you choose to pickup your groceries today?</h1>
      
      {/* puts all options in a wrapper, aligning them horizontally and spacing them out */}
      <div className="wrapper">
        <div className="pickup_methods">
          {/* walking button */}"
          <Link to="/cart" state={{method: "Walking"}}> <button onClick={() => setMethod("Walking")}><img className='walking' src={walking} alt="walking" /></button>  </Link>
          {/* bicycle button */}
          <Link to="/cart" state={{method: "Bicycle"}}> <button onClick={() => setMethod("Bicycle")}><img className='bicycle' src={bicycle} alt="bicycle" /></button> </Link>
          {/* car button */}
          <Link to="/cart" state={{method: "Car"}}> <button onClick={() => setMethod("Car")}><img className='car' src={car} alt="car" /></button> </Link>
        </div>
      </div>
    </div>
  )
}

export default PickUp
