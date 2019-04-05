$(function () {
  var jobID =getQuerystring('job');

  var job = getQuerystring('job');
  var nameFile = "../../jobs/"+job+"/result.json";

  readTextFile(nameFile, function(text){
    var data = JSON.parse(text);
    Highcharts.chart('viewDiagramm', {
      chart: {
          type: 'packedbubble',
          height: '100%'
      },
      title: {
          text: ''
      },
      tooltip: {
          useHTML: true,
          pointFormat: '<b>{point.name}:</b> {point.y} models'
      },
      plotOptions: {
          packedbubble: {
              minSize: '40%',
              maxSize: '100%',
              zMin: 0,
              zMax: 1000,
              layoutAlgorithm: {
                  gravitationalConstant: 0.05,
                  splitSeries: true,
                  seriesInteraction: false,
                  dragBetweenSeries: true,
                  parentNodeLimit: true
              },
              dataLabels: {
                  enabled: true,
                  format: '{point.name}',

                  style: {
                      color: 'black',
                      textOutline: 'none',
                      fontWeight: 'normal'
                  }
              }
          }
      },

      credits:{
      	enabled: false
      },

      series: data

    });
  });

});

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
