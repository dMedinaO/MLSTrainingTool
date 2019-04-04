$(document).ready(function() {

  loadPerformance();

});

//load performance in block
function loadPerformance() {

  var job = getQuerystring('job');
  var nameFile = "../../jobs/"+job+"/performance_model.json";

	readTextFile(nameFile, function(text){
		var data = JSON.parse(text);
    var Spearman = parseFloat(data.Spearman).toFixed(2);
    var R_Score = parseFloat(data.R_Score).toFixed(2);
    var Pearson = parseFloat(data.Pearson).toFixed(2);
    var Kendalltau = parseFloat(data.Kendalltau).toFixed(2);

		$(".rscore").html(R_Score);
		$(".pearson").html(Pearson);
    $(".spearman").html(Spearman);
		$(".kendall").html(Kendalltau);

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
