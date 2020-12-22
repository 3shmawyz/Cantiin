var backend_location="http://127.0.0.1:5000/"


function get_products(in_stock=true)
{
	if (in_stock==true ||in_stock=="true" ||in_stock=="True"||
		in_stock==1||in_stock=="1")
		{in_stock=true;}
	else{in_stock=false;}
	
	method="GET";endpoint="products";
	var settings = getAjaxSettings(method,endpoint,query_inputs=
		{"in_stock":String(in_stock)})
	return $.ajax(settings).done(function(response) {
	  to_return = response;
	});
}
/*
Example:
get_products().then(function(value) {console.log(value);});
it will console.log all the result
*/

function post_products(name,price,in_stock)
{
	if (in_stock==true ||in_stock=="true" ||in_stock=="True"||
		in_stock==1||in_stock=="1")
		{in_stock=true;}
	else{in_stock=false;}
	
	var settings = 
	{
	  "url": backend_location+"products",
	  "method": "POST",
	  "timeout": 0,
	  "headers": 
	  	{
	    	"Content-Type": "application/json"
	  	},
	  "data": JSON.stringify(
	  	{"name":name,"price":price,
	  	"in_stock":in_stock,"seller_id":1}),
	};

	return $.ajax(settings);
}




function delete_products(id)
{
	var settings = 
	{
	  "url": backend_location+"products/"+id,
	  "method": "DELETE"
	};
	return $.ajax(settings);
}






function put_products(id,name,price,in_stock)
{
	if (in_stock==true ||in_stock=="true" ||in_stock=="True"||
		in_stock==1||in_stock=="1")
		{in_stock=true;}
	else{in_stock=false;}
	
	var settings = 
	{
	  "url": backend_location+"products/"+id,
	  "method": "PUT",
	  "timeout": 0,
	  "headers": 
	  	{
	    	"Content-Type": "application/json"
	  	},
	  "data": JSON.stringify(
	  	{"name":name,"price":price,
	  	"in_stock":in_stock,"seller_id":1}),
	};

	return $.ajax(settings);
}









function build_url(endpoint,query_inputs=Array())
{
	var to_return = backend_location + endpoint;
	if (query_inputs.length == 0)
		{return to_return;}
	to_return=to_return+"?";


	for (const property in query_inputs) {
  		to_return=to_return+`${property}=${query_inputs[property]}`+"&";
	}
	to_return=to_return.substring(0,to_return.length-1);
	return to_return;
}

/*
	Example:

  query_parameters={"stock_id":1,"user_id":5}
  console.log(build_url("products",query_inputs=
  query_parameters));

http://127.0.0.1:5000/products?stock_id=1&user_id=5

*/



function getAjaxSettings(method,endpoint,query_inputs={})
{
	url=build_url(endpoint,query_inputs);
	return settings = {"url": url,"method": method};

}
