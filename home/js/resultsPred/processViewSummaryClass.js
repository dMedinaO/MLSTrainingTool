$(document).ready(function() {

	listValuesPerformance();
});

$.fn.DataTable.ext.pager.numbers_length = 5;

//listamos los datos...
var listValuesPerformance = function(){
	var job = getQuerystring('job');
	var url = "../php/queuePred/loadDataCSVPerformancePrediction.php?job="+job;
  var t = $('#jobSummary').DataTable({

      "responsive": true,
      "dom": '<"newtoolbar">frtip',
      "destroy":true,
      "ajax":{
        "method":"POST",
        "url": url
      },

      "columns":[
        {"data":"Algorithm"},
        {"data":"Params"},
        {"data":"R_Score"},
        {"data":"Pearson"},
        {"data":"Spearman"},
				{"data":"Kendalltau"}
      ]
  });
  $('#demo-custom-toolbar3').appendTo($("div.newtoolbar"));

}

//funcion para recuperar la clave del valor obtenido por paso de referencia
function getQuerystring(key, default_) {
  if (default_ == null)
    default_ = "";
  key = key.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
  var regex = new RegExp("[\\?&amp;]"+key+"=([^&amp;#]*)");
  var qs = regex.exec(window.location.href);
  if(qs == null)
    return default_;
  else
    return qs[1];
};
