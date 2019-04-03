$(document).ready(function() {

  showImage();

});

function showImage() {

  var job = getQuerystring('job');

  var url ="../../jobs/"+job+"/world_cloud.svg";
  console.log(url);

  //confusion matriz
  var img = document.getElementById('worldcloudView');
  img.src= "../../jobs/"+job+"/world_cloud.svg";

}
//funcion para recuperar la clave del valor obtenido por paso de referencia
function getQuerystring(key) {
  var url_string = window.location;
	var url = new URL(url_string);
	var c = url.searchParams.get(key);
	return c;
};
