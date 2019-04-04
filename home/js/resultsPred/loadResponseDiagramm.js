$(function () {
  var jobID =getQuerystring('job');

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

    series: [{data: [{name: "Bagging", value: 4}], name: 'Precision'}, {data: [{name: 'NuSVM', value: 14}], name: 'Accuracy'}, {data: [{name: 'Bagging', value: 4}, {name: 'AdaBoostClassifier', value: 3}, {name: 'RandomForestClassifier', value: 8}], name: 'Recall'}, {data: [{name: 'AdaBoostClassifier', value: 1}, {name: 'RandomForestClassifier', value: 4}], name: 'F1'}]

  });
});

//funcion para recuperar la clave del valor obtenido por paso de referencia
function getQuerystring(key) {
  var url_string = window.location;
	var url = new URL(url_string);
	var c = url.searchParams.get(key);
	return c;
};
