$backend_location="http://127.0.0.1:5000/"


function get_products($in_stock=true)
{
	if $in_stock==true:
		$url = backend_location+"products?in_stock=true"
	else:
		$url = backend_location+"products?in_stock=false"
	var settings = {
	  "url": $url,
	  "method": "GET",
	  "timeout": 0
	};
	var to_return="";
	$.ajax(settings).done(function(response) {
	  /*console.log(response);*/to_return=response;
	});
	return to_return;
}