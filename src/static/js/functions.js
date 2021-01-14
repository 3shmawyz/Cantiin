
function changePageHeaderForUser()
{
  document.getElementById("right_top_header_section").innerHTML=
  '     <a href="/manage-products">'+
  '      <button type="button" '+
  '         class="btn btn-success mb-0 mr-2"'+
  '          style="font-weight: bold;font-size: 150%;">'+
  '            My Products'+
  '      </button>'+
  '     </a>'+
  '     <a href="/cart">'+
  '      <button type="button" '+
  '         class="btn btn-success mb-0 mr-2"'+
  '          style="font-weight: bold;font-size: 150%;">'+
  '            My Cart'+
  '      </button>'+
  '     </a>'+
  '      <button type="button" '+
  '         class="btn btn-outline-danger mb-0 mr-2"'+
  '          style="font-weight: bold;font-size: 150%;"'+
  '          onclick="signTheUserOut()">'+
  '            Sign Out'+
  '      </button>';
}


function changeHeaderIfYouSHould()
{
  who().then(function(data, textStatus, xhr) {
        if (xhr.status==200) {changePageHeaderForUser()}});
}

function signTheUserOut()
{
  logout_users().then(
    function(response){
    window.location.href="/";}
    );
}

changeHeaderIfYouSHould();









/*
Cards Templates
*/

/*
product_example=
{
    "id": 1,
    "in_stock": true,
    "name": "Labtop",
    "price": 300.0,
    "seller_id": 1
}
*/


/*
This is the card of the product, created from the product itself 
*/
function home_product_card(input_product)
{
  product_name=input_product["name"];
  product_id = input_product["id"];
  product_price = input_product["price"];
  return '<div class="card mb-4">'+
  '<div class="card-body">'+
    '<h5 class="card-title"'+
    'style="font-weight: bold; font-size: 150%;">'+
    product_name+'</h5>'+
    '<p class="card-text">Price : <b>'+
    product_price+'</b></p>'+
    '<div class="d-flex"><a target="_blank" '+
    'class="stretched-link ml-auto btn btn-outline-success " href="product?id='
    +product_id+'"'+ 
    'class="">'+right_arrow_svg+'</a>'+
    '</div>'+
  '</div>'+
  '</div>'
}



function create_manage_product_card(input_product)
{
  product_name=input_product["name"];
  product_id = input_product["id"];
  product_price = input_product["price"];
  return '<div class="card mb-4" style="">'+
  '  <div class="card-body">'+
  '    <h5 class="card-title"'+ 
  '    style="font-weight: bold; '+
        'font-size: 150%;">'+product_name+'</h5>'+
  '    <p class="card-text">Price :  <b>'+product_price+'</b></p>'+
  '    <div class="d-flex">'+
  '      <a href="edit-product?id='+product_id+
  '" target="_blank" '+
  '       class=" card_button btn btn-outline-warning" '+
  '      style="font-weight: bold;font-size: '+
  '          150%; color: black;">'+
  '        Edit'+
  '      </a>'   +   

  '      <a target="_blank" '+
  '       class="ml-auto card_button btn btn-outline-danger"'+ 
  '      style="font-weight: bold;font-size: 150%"'+
  '      data-toggle="modal" data-target="#exampleModal"'+
  '      onclick="delete_product('+product_id+')" '+
  '      >DELETE'+
  '      </a> '+
  '    </div>'+
  '  </div>'+
  '</div>'
}








/*
Example input:

{
  "amount": 1,
  "id": 1,
  "product": {
      "id": 1,
      "in_stock": true,
      "name": "Labtop",
      "price": 300.0,
      "seller_id": 1
  },
  "total_cost": 300.0,
  "user_id": 1
}

*/


function create_cart_card(input_order)
{

  product_name=input_order["product"]["name"];
  product_price = input_order["product"]["price"];

  amount=input_order["amount"]
  total_cost=input_order["total_cost"]
  order_id=input_order["id"]
  return '<div class="card mb-4" style="">'+
  '  <div class="card-body">'+
  '    <h5 class="card-title"'+ 
  '    style="font-weight: bold; '+
        'font-size: 150%;">'+product_name+'</h5>'+
  '    <p class="card-text">Unit Price :'+
  '       <b>'+product_price+'</b></p>'+
  '    <p class="card-text">Amount (Number of units orders) :'+
  '       <b>'+amount+'</b></p>'+
  '    <div class="d-flex">'+
  '      <span color: black;">'+
  '        Total Price :<b>'+total_cost+'</b>'+
  '      </span>'   +   
  '      <a target="_blank" '+
  '       class="ml-auto card_button btn btn-outline-danger"'+ 
  '      style="font-weight: bold;font-size: 150%"'+
  '      data-toggle="modal" data-target="#exampleModal"'+
  '      onclick="remove_order_from_cart('+order_id+')" '+
  '      >Remove From Cart'+
  '      </a> '+
  '    </div>'+
  '  </div>'+
  '</div>'
}














