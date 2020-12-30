
function changePageHeaderForUser()
{
  document.getElementById("right_top_header_section").innerHTML=
  '      <button type="button" '+
  '         class="btn btn-success mb-0 mr-2"'+
  '          style="font-weight: bold;font-size: 150%;"'+
  '          onclick="window.location.href=\'/manage-products\'">'+
  '            My Products'+
  '      </button>'+
  '      <button type="button" '+
  '         class="btn btn-success mb-0 mr-2"'+
  '          style="font-weight: bold;font-size: 150%;"'+
  '          onclick="window.location.href=\'/cart\'">'+
  '            My Cart'+
  '      </button>'+
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


