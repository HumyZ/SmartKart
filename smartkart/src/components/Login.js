import React from 'react';
import Logo from "./Logo";
import Nav from "./Nav";
import {useState} from 'react';
import {useNavigate} from 'react-router-dom';

{/* responsible for login page */}
function Login() {
     const [email, setEmail] = useState('');
     const [password, setPassword] = useState('');
     const navigate = useNavigate();
    {/* handles user's input */}
     async function handleSubmit(e) {
        e.preventDefault();
        const user = {email, password};
        const response = await fetch('/api/login', {
            method:'POST',
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(user)
        }).then((response) => response.json())
        .then((result) => {
          {/* check if credentials are valid */}
          if(result.success){
            alert("You are logged in.");
            navigate('/items', {
              state: {
                email: email,
              }
            });
          } else {
            alert("Please check your login information.");
            navigate('/login')
          }
        })
    }

  {/* displays input window */}
  return (
    <div>
      <Nav />
        <h1> Login </h1>
        <form className='login-form' onSubmit={handleSubmit}>
          <div className='form-inner'>
            <div className="form-group">
              <label htmlFor='email'>Email:</label>
              <input type="email" name = "email" id= "email" value={email} onChange={(e) => setEmail(e.target.value)} />
            </div>
            <div className="form-group">
              <label htmlFor='password'>Password:</label>
              <input type="password" name = "password" id= "password" value={password} onChange={(e) => setPassword(e.target.value)} />
            </div>
            <input type= "submit" value = "Login"/>
          </div>
        </form>
      <Logo/>
    </div>
  )
}

export default Login
