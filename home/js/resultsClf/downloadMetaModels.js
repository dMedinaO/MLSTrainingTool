$(document).ready(function() {

  downloadDocument();

});

//function download document
function downloadDocument() {

  $("#downloadAnchorElem").on("click", function(){

    var job = getQuerystring('job');
    var nameFile = "../../jobs/"+job+"/meta_models.json";

    readTextFile(nameFile, function(text){
      var dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(text);
      var dlAnchorElem = document.getElementById('downloadAnchorElem');
      dlAnchorElem.setAttribute("href",     dataStr     );
      dlAnchorElem.setAttribute("download", "meta_models.json");

    });

  });
}
//read document
function readTextFile(file, callback) {
    var rawFile = new XMLHttpRequest();
    rawFile.overrideMimeType("application/json");
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if (rawFile.readyState === 4 && rawFile.status == "200") {
            callback(rawFile.responseText);
        }
    }
    rawFile.send(null);
}

//funcion para recuperar la clave del valor obtenido por paso de referencia
function getQuerystring(key) {
  var url_string = window.location;
	var url = new URL(url_string);
	var c = url.searchParams.get(key);
	return c;
};
