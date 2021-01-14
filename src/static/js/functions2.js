

/*These functions are related to the pages with forms
Like: add_product.html, edit_product.html, login.html, signup.html

These are about handling the inputs of the form.
To connect to the "Result:" in the frontend
*/


function diplayResult(color="success",message="")
{
  document.getElementById("the_result").innerHTML=
  '<span style="color:'+color+';">'+message+'</span>';
}
diplayResult("yellow","Waiting for your input")
function handleResponse(response)
{
  if (response["success"]==true) 
  {window.location.href = after_success}
  else{diplayResult("pink",response["description"]);}
}



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
    '<div class="d-flex"><a target="_blank" class="stretched-link ml-auto btn btn-outline-success " href="product?id='
    +product_id+'"'+ 
    'class="">'+right_arrow_svg+'</a>'+
    '</div>'+
  '</div>'+
  '</div>'
}










