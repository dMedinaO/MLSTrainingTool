<?php

  //include files required
  include("../connection.php");

  //id job
  $jobID = $_REQUEST['jobID'];

  //hacemos la consulta a la base de datos y obtenemos la data de interes
  $query = "select COUNT(*) as cantidad from jobData where jobData.idjobData = $jobID";
  $resultado = mysqli_query($conexion, $query);

  $countElement = mysqli_fetch_assoc($resultado)['cantidad'];

  $responseArray = [];

  if ($countElement == 0){
    $responseArray['res'] = 0;
    $responseArray['msg'] = "There are not job registered in system with ID: ".$jobID." please check input value";
  }else{

    #obtenemos la informacion del job
    $query2 = "select * from jobData where jobData.idjobData = $jobID";
    $resultValue = mysqli_query($conexion, $query2);
    $response = mysqli_fetch_assoc($resultValue);

    #formamos la respuesta dependiendo del estado del job
    if ($response['statusJob'] == 'START'){
      $responseArray['res'] = 1;
      $responseArray['msg'] = "Job ID: ".$jobID." is in START status, any change will be notified by email";
    }

    if ($response['statusJob'] == 'PROCESSING'){

      $responseArray['res'] = 2;
      $responseArray['msg'] = "Job ID: ".$jobID." is in  PROCESSING status, any change will be notified by email";
    }

    if ($response['statusJob'] == 'FINISH'){

      $responseArray['res'] = 3;
      $responseArray['kind'] = $response['kind'];
    }
  }

  echo json_encode($responseArray);
?>
