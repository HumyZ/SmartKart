import React from 'react'
import {Link} from 'react-router-dom'
import cart from './images/cart.png';



{/* responsible for changing pages when certain buttons are clicked */}
function Nav() {
  const navStyle = {
    color: 'white'
  }
  return (
    <>
    <nav>
        <h1 >SmartKart</h1>
        <ul className='nav-links'>
        {/* transfers to home page */}
        <Link style={navStyle}  to="/"> <li> Home </li> </Link>
        {/* transfers to shopping page */}
        <Link style={navStyle} to= "/items"> <li> Start Shopping</li> </Link>
        {/* transfers to login page */}
        <Link style={navStyle}  to="/login"> <li> Login </li> </Link>
        {/* transfers to sign up page */}
        <Link style={navStyle} to= "/signup"> <li> Sign Up</li> </Link>
        {/* transfers to pickup page */}
        <Link style={navStyle} className='cart' to= "/pickup">
        <img src={cart} className="cart" /> </Link>
        </ul>   
    </nav>

    <foodnav>
      <ul className='nav-links'>
      </ul>
    </foodnav>
    </>
  )
}

export default Nav
