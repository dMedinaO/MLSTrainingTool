<?php

  #session_start();
  #$idUSer = $_SESSION['idUser'];
  $idUSer = "1";

  include("../connection.php");
  include("../readDocument.php");
  include("../checkResultDB.php");

  #recibimos los parametros...
  $email = $_REQUEST['email'];
  $nameJob = $_REQUEST['nameJob'];
  $descJob = $_REQUEST['descJob'];
  $optionProcess = $_REQUEST['optionProcess'];

  $kind="";

  if($optionProcess == 1){
    $kind="CLASSIFICATION";
  }else{
    $kind="PREDICTION";
  }

  #obtenemos los datos desde la sesion...

  $idJob = time();#sera el id del job...
  $response ['job'] = $idJob;

  $pathRespone = "/var/www/html/MLSTrainingTool/jobs/";
  #obtenemos el nombre del archivo de entrada...
  $pathData = "/var/www/html/MLSTrainingTool/jobs/tmp/".$idUSer."_documentQueue.txt";
  $nameDocument = readDocument($pathData);
  $response ['nameFile'] = $nameDocument;

  #hacemos la insercion a la base de datos...
  $query = "insert into jobData values ($idJob, '$nameJob', '$descJob', '$email', 0, NOW(), NOW(), 'INIT', 'INIT JOB', '$kind', '$nameDocument')";
  $resultado = mysqli_query($conexion, $query);
  $requestData = verificar_resultado($resultado);

  $response ['queriesInsert'] = $query;

  if ($requestData == "BIEN"){#movemos el archivo de tmp al path del usuario y ejecutamos el proceso solo si la opcion de algorithm es todos...

    #movemos el archivo... creamos directorio
    $path = "/var/www/html/MLSTrainingTool/jobs/$idJob";

    if (!file_exists($path)) {
        mkdir($path, 0777, true);
    }

    #movemos el archivo...
    //movemos el archivo al path de la licitacion...
    $pathActual = "/var/www/html/MLSTrainingTool/jobs/tmp/$nameDocument";
    $pathMove = "/var/www/html/MLSTrainingTool/jobs/$idJob/";

    $command = "mv $pathActual $pathMove";
    $pathDataSet ="/var/www/html/MLSTrainingTool/jobs/$idJob/$nameDocument";
    exec($command);

    //ejecutamos el script python que permite el analisis de las caracteristicas
    $command = "python /var/www/html/MLSTrainingTool/models/bin/launcherCheckFeature.py $pathDataSet $idJob";
    $response['command'] = $command;
    exec($command);

    $response['exec'] = "OK";

  }else{
    $response['exec'] = "ERROR";

  }

  echo json_encode($response);

?>
