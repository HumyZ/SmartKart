import React from 'react'
import {Link} from 'react-router-dom'
import cart from './images/cart.png';
import Table from './Table';
import { useLocation } from 'react-router-dom'
import {useState, useEffect} from 'react';

function Cart() {
  const navStyle = {
    color: 'white'
  };
  const location = useLocation()
  const { method } = location.state

  useEffect(() => {
    displayCart();
  }, []);



  const url = '/api/cart/breakdown?method=' + method;

  async function displayCart(e){
    var container = document.getElementById("receiptContainer") ;
    container.innerHTML = "<b>Loading...</b>";
    const response = await fetch(url, {
        method:'GET',
        headers: {"Content-Type": "application/json"}
    }).then((response) => response.json())
    .then((result) => {
      console.log(result);

      container.innerHTML = "";

      result.stores.forEach(function(store) {
        console.log(store.name);
        console.log(store.subtotal);
        console.log(store.distance);
        console.log(store.time);
        var distance = store.distance;
        var time = store.time;
        let gas_rate = 1.24;
        var gas_cost = (parseFloat(distance.slice(0, -3))/100)*gas_rate;


        var receipt = document.createElement("div");
        receipt.className = "receipt";
        let label = document.createElement("label");
        label.className = 'store_name';
        label.innerHTML = store.name

        let table = document.createElement("table");

        let row = table.insertRow(0);
        let cell_category = row.insertCell(0);
        let cell_name = row.insertCell(1);
        let cell_quantity = row.insertCell(2);
        let cell_price = row.insertCell(3);
        cell_category.innerHTML = "Item Category";
        cell_name.innerHTML = "Item name";
        cell_quantity.innerHTML = "Quantity";
        cell_price.innerHTML = "Price";

        var i = 1;
        store.items.forEach(function(item) {
          console.log(item);
          let row = table.insertRow(i);
          let cell_category = row.insertCell(0);
          let cell_name = row.insertCell(1);
          let cell_quantity = row.insertCell(2);
          let cell_price = row.insertCell(3);
          cell_category.innerHTML = item.item_category;
          cell_name.innerHTML = item.item_name;
          cell_quantity.innerHTML = item.quantity;
          cell_price.innerHTML = item.item_price;
          i += 1;
        });

        let label_pickupoption = document.createElement("label");
        label_pickupoption.className = 'receipt_details';
        label_pickupoption.innerHTML = 'Pickup Option Chosen: ' + method + ' <br>' ;

        let label_distance = document.createElement("label");
        label_distance.className = 'receipt_details';
        label_distance.innerHTML = 'Distance: ' + distance + '<br>';

        let label_time = document.createElement("label");
        label_time.className = 'receipt_details';
        label_time.innerHTML = 'Time: ' + time + '<br>';

        let label_cost = document.createElement("label");

        if (method == "Car"){
          label_cost.className = 'receipt_details';
          label_cost.innerHTML ='Gas cost: ' + gas_cost + ' <br>' ;
        }


        let br = document.createElement("br");

        let label_totalcost = document.createElement("label");
        label_totalcost.className = 'receipt_details';
        label_totalcost.innerHTML = 'Sub Total: ' + store.subtotal + ' <br>';

        receipt.appendChild(label);
        receipt.appendChild(table);
        receipt.appendChild(label_pickupoption);
        receipt.appendChild(label_distance);
        receipt.appendChild(label_time);
        receipt.appendChild(label_totalcost);
        if (method == "Car"){
          receipt.appendChild(label_cost);
        }

        container.appendChild(receipt);



      }


      )

    })

  }




  return (
    <div>
      <nav>
        <h1 >SmartKart</h1>
        <ul className='nav-links'>
        {/* transfers to home page */}
        <Link style={navStyle}  to="/"> <li> Home </li> </Link>
        {/* transfers to shopping page */}
        <Link style={navStyle} to= "/items"> <li> Continue Shopping</li> </Link>
        {/* transfers to pickup page */}
        <Link style={navStyle} className='cart' to= "/pickup">
        <img src={cart} className="cart" /> </Link>
        </ul>
    </nav>
    <h1> Your store options:</h1>


    <div id="receiptContainer" className='receiptContainer'>

    </div>

    </div>
  )
}

export default Cart
