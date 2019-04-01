$(document).ready(function() {

  //creamos los histogramas
  histogramFunction('Precision', 'precisionHistogram');
  histogramFunction('Recall', 'recallHistogram');
  histogramFunction('F1', 'f1Histogram');
  histogramFunction('Accuracy', 'accuracyHistogram');

  //cargamos las definiciones de las medidas
  definitions();
  definitionsProcess();
});

//funcion para recuperar la clave del valor obtenido por paso de referencia
function getQuerystring(key) {
  var url_string = window.location;
	var url = new URL(url_string);
	var c = url.searchParams.get(key);
	return c;
};

var histogramFunction = function(key, plot){

  var job = getQuerystring('job');


    var url = "../../jobs/"+job+"/summaryProcessJob_"+job+".csv";
    Plotly.d3.csv(url, function(err, rows){

      function unpack(rows, key) {
          return rows.map(function(row) {
            return row[key.replace('.',' ')];
          });
      }

      var trace1 = {
        x: unpack(rows,key),
        name: 'Performance',
        autobinx: true,
        histnorm: "count",
        marker: {
          color: "rgba(100, 150, 102, 0.7)",
          line: {
            color:  "rgba(100, 150, 102, 1)",
            width: 1
          }
        },
        opacity: 0.5,
        type: "histogram",
      };

      var data = [trace1];
      var layout = {
        bargap: 0.05,
        bargroupgap: 0.2,
        barmode: "overlay",
        xaxis: {title: "Value"},
        yaxis: {title: "Frequence"}
      };
      Plotly.newPlot(plot, data, layout);

    });
}

var definitions = function loadDefinition() {

  var nameFile = "../resourceData/dataDefinitions.json";

	readTextFile(nameFile, function(text){
		var data = JSON.parse(text);
		$(".precisionDefinition").html(data.definitionPerformanceCla[0].definition);
		$(".accuracyDefinition").html(data.definitionPerformanceCla[1].definition);
    $(".recallDefinition").html(data.definitionPerformanceCla[2].definition);
		$(".f1Definition").html(data.definitionPerformanceCla[4].definition);

	});

}

var definitionsProcess = function loadDefinitionProcess() {

  var job = getQuerystring('job');

    var urlFile = "../../jobs/"+job+"/summaryProcess_"+job+".json";
  	readTextFile(urlFile, function(text){
  		var data = JSON.parse(text);

      var duration = parseFloat(data.ejecucion)/(60*60);

  		$(".start").html(data.inicio);
  		$(".end").html(data.termino);
      $(".correct").html(data.iteracionesCorrectas);
  		$(".incorrect").html(data.iteracionesIncorrectas);
      $(".duration").html(duration);
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
