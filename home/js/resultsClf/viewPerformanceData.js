$(document).ready(function() {

  loadPerformance();

});

//load performance in block
function loadPerformance() {

  var job = getQuerystring('job');
  var nameFile = "../../jobs/"+job+"/performance_model.json";
  console.log(nameFile);
	readTextFile(nameFile, function(text){
		var data = JSON.parse(text);
    var precision = parseFloat(data.Precision).toFixed(4)*100;
    var accuracy = parseFloat(data.Accuracy).toFixed(4)*100;
    var recall = parseFloat(data.Recall).toFixed(2);
    var f1Score = parseFloat(data.F1).toFixed(2);

		$(".precision").html(precision);
		$(".accuracy").html(accuracy);
    $(".recall").html(recall);
		$(".f1Values").html(f1Score);

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
