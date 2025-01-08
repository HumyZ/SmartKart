import React from 'react'
import Logo from "./Logo";
import Nav from "./Nav";
import {useState} from 'react';
import {useNavigate} from 'react-router-dom';

{/* responsible for signup page */}
const Signup = () => {
    const [first_name, setFirstName] = useState('');
    const [last_name, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [postal_code, setPostalCode] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate() ;

    {/* handles user's input */}
    async function handleSubmit(e) {
        e.preventDefault();
        const user = {first_name, last_name, email, postal_code, password};
        const response = await fetch('/api/login/register', {
            method:'POST',
            headers: {"Content-Type": "application/json"}, 
            body: JSON.stringify(user)
        })
        {/* checks if credentials are valid, and responds accordingly */}
        const json = await response.json();
        if (json.success){
           alert("You have created a new account.");
           navigate('/items');
        }
        else {
            alert("Please check the information entered.");
            navigate('/signup');
        }
    }

  return (
    <div className='Signup'>
       <Nav />
       <h2> Welcome to SmartKart</h2>
       <h3>  Enter your details to get started!</h3>
        {/* handles user's input*/}
        <form className='login-form' onSubmit={handleSubmit}>
        {/* all input boxes of signup page */}
        <div className='form-inner'>
            <div className="form-group">
                {/* input for first name name */}
                <label htmlFor='name'> First Name:</label>
                <input type="text" name = "first_name" id= "first_name" value={first_name} onChange={(e) => setFirstName(e.target.value)}/>
            </div>
            {/* input for last name */}
            <div className="form-group">
                <label htmlFor='name'> Last Name:</label>
                <input type="text" name = "last_name" id= "last_name" value={last_name} onChange={(e) => setLastName(e.target.value)} />
            </div>
            {/* input for email */}
            <div className="form-group">
                <label htmlFor='email'> Email:</label>
                <input type="email" name = "email" id= "email" value={email} onChange={(e) => setEmail(e.target.value)}/>
            </div>
            {/* input for postal code */}
            <div className="form-group">
                <label htmlFor='postal-code'> Postal Code:</label>
                <input type="text" name = "postal-code" id= "postal-code" value={postal_code} onChange={(e) => setPostalCode(e.target.value)}/>

            </div>
            {/* input for password */}
            <div className="form-group">
                <label htmlFor='password'> Password:</label>
                <input type="password" name = "password" id= "password" value={password} onChange={(e) => setPassword(e.target.value)}/>

            </div>
            {/* signup button */}
            <input type= "submit" value = "Sign Up"/>
        </div>
        </form> 
        <Logo/>
    </div>
  )
}


export default Signup