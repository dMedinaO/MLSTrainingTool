$(document).ready(function() {

  //hacemos las lecturas de las tablas
  listModelsR_Score();
  listModelsSpearman();
  listModelsPearson();
  listModelsKendalltau();
});

$.fn.DataTable.ext.pager.numbers_length = 5;

//listamos los datos...
var listModelsR_Score = function(){
	var job = getQuerystring('job');
	var url = "../php/queuePred/loadValuesPerformance.php?job="+job+"&feature=R_Score";
  var t = $('#modelR_Score').DataTable({

      "responsive": true,
      "dom": '<"newtoolbar">frtip',
      "destroy":true,
      "order": [[ 2, "desc" ]],
      "ajax":{
        "method":"POST",
        "url": url
      },

      "columns":[
        {"data":"Algorithm"},
        {"data":"Params"},
				{"data":"R_Score"},
      ]
  });
  $('#demo-custom-toolbar4').appendTo($("div.newtoolbar"));

}

//listamos los datos...
var listModelsPearson = function(){
	var job = getQuerystring('job');
	var url = "../php/queuePred/loadValuesPerformance.php?job="+job+"&feature=Pearson";
  var t = $('#modelPearson').DataTable({

      "responsive": true,
      "dom": '<"newtoolbar">frtip',
      "destroy":true,
      "order": [[ 2, "desc" ]],
      "ajax":{
        "method":"POST",
        "url": url
      },

      "columns":[
        {"data":"Algorithm"},
        {"data":"Params"},
				{"data":"Pearson"},
      ]
  });
  $('#demo-custom-toolbar5').appendTo($("div.newtoolbar"));

}

//listar modelos de accuracy
var listModelsSpearman = function(){
	var job = getQuerystring('job');
	var url = "../php/queuePred/loadValuesPerformance.php?job="+job+"&feature=Spearman";
  var t = $('#modelSpearman').DataTable({

      "responsive": true,
      "dom": '<"newtoolbar">frtip',
      "destroy":true,
      "order": [[ 2, "desc" ]],
      "ajax":{
        "method":"POST",
        "url": url
      },

      "columns":[
        {"data":"Algorithm"},
        {"data":"Params"},
				{"data":"Spearman"},
      ]
  });
  $('#demo-custom-toolbar6').appendTo($("div.newtoolbar"));

}

//listar modelos de F1
var listModelsKendalltau = function(){
	var job = getQuerystring('job');
	var url = "../php/queuePred/loadValuesPerformance.php?job="+job+"&feature=Kendalltau";
  var t = $('#modelKendalltau').DataTable({

      "responsive": true,
      "dom": '<"newtoolbar">frtip',
      "destroy":true,
      "order": [[ 2, "desc" ]],
      "ajax":{
        "method":"POST",
        "url": url
      },

      "columns":[
        {"data":"Algorithm"},
        {"data":"Params"},
				{"data":"Kendalltau"},
      ]
  });
  $('#demo-custom-toolbar7').appendTo($("div.newtoolbar"));

}

//funcion para recuperar la clave del valor obtenido por paso de referencia
function getQuerystring(key) {
  var url_string = window.location;
	var url = new URL(url_string);
	var c = url.searchParams.get(key);
	return c;
};
