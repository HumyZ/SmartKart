import React from 'react'
import img_2 from './images/grocery_cart.png';
import nofrills_logo from './images/nofrills_logo.svg';
import zehrs_logo from './images/zehrz_logo.png';
import longos_logo from './images/longos-logo.png';
import loblaws_logo from './images/Loblaws_logo-promo.jpeg';
import Nav from "./Nav";
import {useState} from 'react';
import {useNavigate} from 'react-router-dom';

//function responsible for home page
function Home() {
  const [postal_code, setPostalCode] = useState('');
  const navigate = useNavigate() ;

  {/* handles user's postal code input */}
  async function handleSubmit(e) {
    e.preventDefault();
    const code = {"location":postal_code}
    const response = await fetch('/api/location', {
        method:'POST',
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(code)
    }).then((response) => response.json())
    .then((result) => {
      {/* check if credentials are valid */}
      if(result.success){
        alert("Postal Code Entered");
        navigate('/items', {
          state: {
            postal_code: postal_code,
          }
        });
      } else {
        alert("Incorrect Postal code");
        navigate('/')
      }
    })
}

  return (
    <div className='Home'>
      <Nav />
      {/* Orange banner across home screen */}
      {/* Input for postal code */}
      <form className="form-postal-code" onSubmit={handleSubmit} >
            <label htmlFor='item'>Postal code: </label>
            <input type="text" name = "postal-code" id= "postal-code" value={postal_code} onChange={(e) => setPostalCode(e.target.value)} />
          </form>
      <div className="Home-block">
        {/* Tagline */}
        <div className="tagline">
          <p>Find groceries that suit your budget!</p>
        </div>
      </div>
      {/* Image of grocery bag with checklist */}
      <img className='top-image' src={img_2} alt="Image 1" />
      <h4>Grocery stores we offer:</h4>
      {/* Walmart Logo */}
      <div className='logos'>
      <img className='grocery_store_logo' src={loblaws_logo} alt="Image 1"  />  
      <img className='grocery_store_logo' src={nofrills_logo} alt="Image 1"  />  
      <img className='grocery_store_logo' src={zehrs_logo} alt="Image 1"  />  
      </div>

    </div>
  )
}
export default Home
