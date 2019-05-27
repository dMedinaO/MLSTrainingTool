<?php

  include("../connection.php");
  include("../checkResultDB.php");

  #recibimos los parametros...
  $job = $_REQUEST['job'];
  $kind = $_REQUEST['kind'];//1. clf, 2. regx
  $responseData = $_REQUEST['response'];
  $remove = $_REQUEST['removeOutliers'];//1. NO, 2. SI

  $response = [];

  #hacemos la insercion a la base de datos en la tabla response
  $query = "insert into response values (NULL, '$responseData', $job, $remove, $kind)";
  $response['insert'] = $query;
  $resultado = mysqli_query($conexion, $query);
  $requestData = verificar_resultado($resultado);

  //chequeamos si quedo OK
  if ($requestData == "BIEN"){

    //cambiamos los datos en la DB
    $query = "update jobData set statusJob = 'START', dateInit=NOW() where idjobData=$job";
    $resultado = mysqli_query($conexion, $query);
    $requestData2 = verificar_resultado($resultado);
    if ($requestData2){
        $response['execResponse'] = "OK";
    }else{
      $response['execResponse'] = "ERROR";
    }
  }else{
    $response['execResponse'] = "ERROR";
  }

  echo json_encode($response);

?>
