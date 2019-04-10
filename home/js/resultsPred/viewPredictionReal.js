$(function () {
  var job = getQuerystring('job');
  var nameFile = "../../jobs/"+job+"/prediction_data.json";

  readTextFile(nameFile, function(text){
    var data = JSON.parse(text);

    var valuesPredict = data.prediccion;
    var valuesReal = data.real;

    var xValues = [];

    //generamos el array con las x...
    for (i=0;i<valuesReal.length; i++){
      xValues.push(i+1);

    }
    createGraphicData(valuesReal, valuesPredict, xValues)

  });
});

//funcion para cargar el grafico
function createGraphicData(valuesReal, valuesPredict, xValues){

	var trace1 = {
		x: xValues,
	  y: valuesReal,
	  mode: 'markers',
	  type: 'scatter',
		name: 'Real Values'
	};

	var trace2 = {
		x: xValues,
	  y: valuesPredict,
	  mode: 'lines+markers',
	  type: 'scatter',
		name: 'Predict Values',
		line: {
      line: {shape: 'spline'}
    },
	};

	var data = [trace1, trace2];

	Plotly.newPlot('predictionReal', data);

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
