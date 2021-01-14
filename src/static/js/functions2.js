

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