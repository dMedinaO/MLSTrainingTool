$(function () {
  var jobID =getQuerystring('job');
	var processed_json = new Array();
  var url = '../php/queue/showDistributionClf.php?job='+jobID;
  console.log(url);
	$.getJSON(url, function(data) {

    console.log(data);

		// Populate series
		for (i = 0; i < data.length; i++){
			var cantidad = parseInt(data[i].value);
			processed_json.push([data[i].performance, cantidad]);
		}
    console.log("response");
    console.log(processed_json);
		// draw chart
      $('#distributionPerformanceModel').highcharts({
				chart: {
					plotBackgroundColor: null,
					plotBorderWidth: null,
					plotShadow: false,
					type: 'pie'
				},

				plotOptions: {
					pie: {
						allowPointSelect: true,
						cursor: 'pointer',
						dataLabels: {
							enabled: false
						},
						showInLegend: true
					}
				},
				credits: {
				  enabled: false
				},

				title: {
					text: ""
				},

		           series: [{
					name: 'Performance',
		               data: processed_json
				}]
			});
	});
});

//funcion para recuperar la clave del valor obtenido por paso de referencia
function getQuerystring(key) {
  var url_string = window.location;
	var url = new URL(url_string);
	var c = url.searchParams.get(key);
	return c;
};
