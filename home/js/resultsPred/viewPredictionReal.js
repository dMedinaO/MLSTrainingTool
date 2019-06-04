$(function () {
  var job = getQuerystring('job');
  var nameFile = "../../jobs/"+job+"/prediction_data.json";

  readTextFile(nameFile, function(text){
    var data = JSON.parse(text);

    var valuesPredict = data.prediccion;
    var valuesReal = data.real;

    var xValues = [];
    var errorGraphic = [];

    //generamos el array con las x...
    for (i=0;i<valuesReal.length; i++){
      xValues.push(i+1);
      errorGraphic[i] = (valuesReal[i]-valuesPredict[i]);
    }
    createGraphicData(valuesReal, valuesPredict, xValues)
    createGraphicDataOnlyTrace(errorGraphic, xValues);

  });
});

//funcion para cargar el grafico
function createGraphicDataOnlyTrace(values, xValues){

	var trace2 = {
		x: xValues,
	  y: values,
	  mode: 'markers',
		name: 'Error Values',
		line: {
      line: {shape: 'spline'}
    },
    marker: {
      color: 'rgb(142, 124, 195)',
      size: 8
    }
	};

  var layout = {
    xaxis:{
      title: "Elements"
    },

    yaxis:{
      title: "Error values"
    }
  };

	var data = [trace2];

	Plotly.newPlot('errorData', data, layout);

}

//funcion para cargar el grafico
function createGraphicData(valuesReal, valuesPredict, xValues){

	var trace1 = {
		x: valuesReal,
	  y: valuesPredict,
	  mode: 'markers',
	  type: 'scatter',
    marker: {
      color: 'rgb(142, 124, 195)',
      size: 8
    }
	};

  var layout = {
    xaxis:{
      title: "Real Values"
    },

    yaxis:{
      title: "Prediction Values"
    }
  }
	var data = [trace1];

	Plotly.newPlot('predictionReal', data, layout);

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
