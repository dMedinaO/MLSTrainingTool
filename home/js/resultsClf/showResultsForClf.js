$(document).ready(function() {

  loadGraphics();

});

function loadGraphics() {

  var job = getQuerystring('job');
  var nameFile = "../../jobs/"+job+"/confusionMatrix.json";

  readTextFile(nameFile, function(text){
    var data = JSON.parse(text);

    //hacemos el grafico de fiabilidad y bakanosidad
    var xData = data.header;
/*
    var trace1 = {
      x: xData,
      y: data.matrixConfusionResponse.fiabilidad,
      name: 'Reliability',
      type: 'bar'
    };

    var trace2 = {
      x: xData,
      y: data.matrixConfusionResponse.bakanosidad,
      name: 'Bakanosidad',
      type: 'bar'
    };

    var dataLa = [trace1, trace2];

    var layout = {barmode: 'group'};

    Plotly.newPlot('fiabilidad', dataLa, layout);
*/
    //hacemos el heat map de la matriz de confusion
    var colorscaleValue = [
      [0, '#3D9970'],
      [1, '#001f3f']
    ];
    var dataHeat = [
      {
        z: data.matrix,
        x: xData,
        y: xData,
        type: 'heatmap',
        colorscale: colorscaleValue
      }
    ];

    var layout = {

      annotations: [],
      xaxis: {
        title: 'Prediction Values',
      }

    };

    for ( var i = 0; i < xData.length; i++ ) {
      for ( var j = 0; j < xData.length; j++ ) {
        var currentValue = data.matrix[i][j];
        if (currentValue != 0.0) {
          var textColor = 'white';
        }else{
          var textColor = 'black';
        }
        var result = {
          xref: 'x1',
          yref: 'y1',
          x: xData[j],
          y: xData[i],
          text: data.matrix[i][j],
          font: {
            family: 'Arial',
            size: 16,
            color: 'rgb(50, 171, 96)'
          },
          showarrow: false,
          font: {
            color: textColor
          }
        };
        layout.annotations.push(result);
      }
    }

    Plotly.newPlot('confusionMatrixGraph', dataHeat, layout);
  });

}
//funcion para recuperar la clave del valor obtenido por paso de referencia
function getQuerystring(key) {
	var url_string = window.location;
	var url = new URL(url_string);
	var c = url.searchParams.get(key);
	return c;
};

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
