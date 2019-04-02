$(document).ready(function() {

  //hacemos las lecturas de las tablas
  listModelsP();
  listModelsA();
  listModelsR();
  listModelsF();
});

$.fn.DataTable.ext.pager.numbers_length = 5;

//listamos los datos...
var listModelsP = function(){
	var job = getQuerystring('job');
	var url = "../php/queue/loadValuesPerformance.php?job="+job+"&feature=Precision";
  var t = $('#modelP').DataTable({

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
				{"data":"Precision"},
      ]
  });
  $('#demo-custom-toolbar4').appendTo($("div.newtoolbar"));

}

//listamos los datos...
var listModelsR = function(){
	var job = getQuerystring('job');
	var url = "../php/queue/loadValuesPerformance.php?job="+job+"&feature=Recall";
  var t = $('#modelR').DataTable({

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
				{"data":"Recall"},
      ]
  });
  $('#demo-custom-toolbar5').appendTo($("div.newtoolbar"));

}

//listar modelos de accuracy
var listModelsA = function(){
	var job = getQuerystring('job');
	var url = "../php/queue/loadValuesPerformance.php?job="+job+"&feature=Accuracy";
  var t = $('#modelA').DataTable({

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
				{"data":"Accuracy"},
      ]
  });
  $('#demo-custom-toolbar6').appendTo($("div.newtoolbar"));

}

//listar modelos de F1
var listModelsF = function(){
	var job = getQuerystring('job');
	var url = "../php/queue/loadValuesPerformance.php?job="+job+"&feature=F1";
  var t = $('#modelF').DataTable({

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
				{"data":"F1Score"},
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
