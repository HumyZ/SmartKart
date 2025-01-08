import React from 'react';
import {Link} from 'react-router-dom';
import styled from 'styled-components';
import Nav from "./Nav";
import fruits from './images/Fruits.jpg';
import beverages from './images/beverages.png';
import dairy from './images/Dairy.jpg';
import meat from './images/Meat.jpg';
import household from './images/household.png';
import longos_flyer1 from './images/flyers/longos_flyer1.png';
import longos_flyer2 from './images/flyers/longos_flyer2.png';
import nofrills_flyer1 from './images/flyers/nofrills_flyer1.png';
import nofrills_flyer2 from './images/flyers/nofrills_flyer2.png';
import zehrs_flyer1 from './images/flyers/zehrs_flyer1.png';
import zehrs_flyer2 from './images/flyers/zehrs_flyer2.png';
import {useState, useEffect} from 'react';

import {useNavigate} from 'react-router-dom';
import Cart from './Cart';


{/* responsible for items page */}
function Items() {
  const [category, setCategory]= useState("");
  const [items, setItems]= useState([]);
  const [itemName, setItemName] = useState("");
  const [itemPriceRange, setItemPriceRange] = useState("");
  const [itemStores, setItemStore] = useState("");
  const [isOpen, setIsOpen] = useState(false);
  const [itemQuantity, setItemQuantity] = useState("");





  const navigate = useNavigate();

  {/* Waits for setCategory to set category state before calling the handleSubmit function */}
  useEffect(() => {
    handleSubmit();

}, [category]);


  {/* Displays a pop-up when category is selected */}
  {/* Unique pop-up for each button clicked */}
  const Modal = ({ setIsOpen }) => {
    return (
      <>
        <div className="darkBG" onClick={() => setIsOpen(false)} />
          <div className="centered">
            <div className="modal">
              <div className="modalHeader">
                <h5 className="heading">Item Details</h5>
              </div>
              <button className="closeBtn" onClick={() => setIsOpen(false)}>
              </button>
              <div className="modalContent"> Item Name: {itemName} </div>
              <div className="modalContent"> Price range: {itemPriceRange} </div>
              <div className="modalContent"> Available at Stores: {itemStores} </div>

              <div className="modalActions">
                <div className="actionsContainer">
                  <button
                    className="addBtn"
                    onClick={(e) => {setIsOpen(false); handleAddToCart(e); }}>
                    Add to Cart
                  </button>
                  <input className="itemNumber" type="number" min='1' ></input>
                </div>
              </div>
            </div>
          </div>
      </>
    );
  };
  {/* Handles details for each of the items */}
  function itemDetails(name, price_range, stores){
    setItemName(name);
    setItemPriceRange(price_range);
    setItemStore(stores);
  }

  {/* Retrieves data from backend when a button is clicked */}
  async function handleSubmit(e) {
    const url = '/api/item/?category=' + category;

        const response = await fetch(url, {
            method:'GET',
            headers: {"Content-Type": "application/json"}
        }).then((response) => response.json())
        .then((result) => {

          setItems(arr => [...result.items]);
          console.log(result);
        var container = document.getElementById("itemsContainer") ;
        container.innerHTML = "";

        result.items.forEach(function(item) {
          let item_display = document.createElement("div");
          item_display.className= 'item_image_tag';

          console.log(item);
          console.log(item.item_name);
          console.log(item.price_range);
          {/* loags image thumbnails */}
          let btn = document.createElement("button");
          let label = document.createElement("label");
          let image = document.createElement("img");
          btn.className = "items-link";
          label.className = "item_label";
          btn.onclick = function() {
            setIsOpen(true);
            itemDetails(item.item_name, item.price_range, item.stores);
          }

          image.setAttribute("src", item.url);
          image.setAttribute("referrerpolicy", "no-referrer");
          btn.appendChild(image);
          label.innerHTML = item.item_name;
          item_display.appendChild(btn);
          item_display.appendChild(label);
          container.appendChild(item_display);

        });
        })
}

 {/* Handles details for each of the items */}
 function itemDetails(name, price_range, stores){
  setItemName(name);
  setItemPriceRange(price_range);
  setItemStore(stores);
}

{/* Retrieves data from backend when search button is clicked */}
async function handleSearch(e) {
  e.preventDefault();
  var search = document.getElementsByClassName("search_item");
  const url = '/api/item/?name=' + encodeURIComponent( search[0].value);

  const response = await fetch(url, {
    method:'GET',
    headers: {"Content-Type": "application/json"}
}).then((response) => response.json())
.then((result) => {

  setItems(arr => [...result.items]);
  console.log(result);
var container = document.getElementById("itemsContainer") ;
container.innerHTML = "";

result.items.forEach(function(item) {
  let item_display = document.createElement("div");
  item_display.className= 'item_image_tag';

  console.log(item);
  console.log(item.item_name);
  console.log(item.price_range);
  {/* loags image thumbnails */}
  let btn = document.createElement("button");
  let label = document.createElement("label");
  let image = document.createElement("img");
  btn.className = "items-link";
  label.className = "item_label";
  btn.onclick = function() {
    setIsOpen(true);
    itemDetails(item.item_name, item.price_range, item.stores);
  }

  image.setAttribute("src", item.url);
  image.setAttribute("referrerpolicy", "no-referrer");
  btn.appendChild(image);
  label.innerHTML = item.item_name;
  item_display.appendChild(btn);
  item_display.appendChild(label);
  container.appendChild(item_display);

});
})
}




async function handleAddToCart(e){

  var number = document.getElementsByClassName("itemNumber");
  const item_url = 'api/cart/add/' + itemName + '?n=' + number[0].value;
  const response = await fetch(item_url, {
      method:'GET',
      headers: {"Content-Type": "application/json"}
  }).then((response) => response.json())
  .then((result) => {
    {/* check if credentials are valid */}
    if(result.success){
      alert("Item is added to cart.");
      navigate('/items')
    } else {
      alert("Item not added");
      navigate('/items')
    }
  })

}

  return (
    <div>
      <Nav />

      {/* Small buttons near top of page and search bar */}
        <div className='itemsbar' >
          {/* search bar */}

          <form  id="form-item-search" className="form-item-search" onSubmit={handleSearch}>
            <label htmlFor='item'>Search for Item: </label>
            <input type="text" className = "search_item" id= "search_item" />
            <input type= "submit" className='searchbutton' value = "Search"/>
          </form>


          <button className='itemsbutton'> On Sale </button>
          <div className="dropdown">
            <button className="dropbtn">    Filter
              <i className="fa fa-caret-down"></i>
            </button>
            {/* dropdown menu */}
            <div className="dropdown-content">
              <a href="#">Best Match</a>
              <a href="#">Popular</a>
              <a href="#">Price High to Low</a>
              <a href="#">Price Low to High</a>
            </div>
          </div>
        </div>

        {/* boxes where ad flyers are displayed */}
        <div className="box">
           <div className="card-a"> <img src={nofrills_flyer1} ></img> </div>
           <div className="card-a"> <img src={longos_flyer1} ></img> </div>
           <div className="card-a"> <img src={zehrs_flyer1} ></img> </div>
           <div className="card-a"> <img src={nofrills_flyer2} ></img> </div>
           <div className="card-a"> <img src={longos_flyer2} ></img> </div>
           <div className="card-a"> <img src={zehrs_flyer2} ></img> </div>

       </div>



      {/* container boxes for items being displayed after search */}
      <div id="itemsContainer" className='itemsContainer'>
     


      </div>
      <div id="receiptContainer" className='receiptContainer'> </div>

      <h1>
        Categories
      </h1>

      {/* handles the setting of state for the modal class */}
      {isOpen && <Modal setIsOpen={setIsOpen} />}
      {/* puts all buttons in a wrapper, aligning them horizontally and spacing them out */}
      <div className="wrapper">
        {/* fruits and vegetables button */}
        <div className="box2">
          <foodnav>
          <button onClick={() => setCategory("Fruits%20and%20Vegetables")}><img className='fruits' src={fruits} alt="fruits"  />
              <h2>Fruits and Vegetables </h2>
              </button>

          </foodnav>


        </div>
        {/* beverages button category*/}
        <div className="box2">
          <foodnav>
          <button onClick={() => setCategory("Beverages")}  ><img className='beverages' src={beverages} alt="beverages" />
            <h2>Beverages</h2>
            </button>

          </foodnav>

        </div>
        {/* dairy button category */}
        <div className="box2">
          <foodnav>
          <button onClick={() => setCategory("Dairy")}><img className='dairy' src={dairy} alt="dairy" />
            <h2>Dairy</h2>
            </button>

          </foodnav>



        </div>
        {/* meat button category*/}
        <div className="box2">
         <foodnav>
         <button onClick={() =>setCategory("Meat")}><img className='meat' src={meat} alt="meat" />
          <h2>Meat</h2>
          </button>

         </foodnav>



        </div>
        {/* household/cleaning category button */}
        <div className="box2">
          <foodnav>
          <button onClick={() =>setCategory("Household/Cleaning")}><img className='household' src={household} alt="Household/Cleaning" />
          <h2>Household/Cleaning</h2>
          </button>

          </foodnav>


        </div>
      </div>

    </div>



 )
  }

export default Items
