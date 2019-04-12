<?php

  #include files required
  include("../connection.php");
  include("../readDocument.php");

  #id job
  $jobID = $_REQUEST['job'];

  #obtenemos el nombre del set de datos
  $nameDocument = readDocument("/var/www/html/MLSTrainingTool/jobs/tmpTry/1_documentQueue.txt");

  #lo movemos al directorio del job
  $command = "mv /var/www/html/MLSTrainingTool/jobs/tmpTry/".$nameDocument. " /var/www/html/MLSTrainingTool/jobs/".$jobID;
  exec($command);

  #hacemos la consulta a la base de datos y obtenemos la data del set de datos asociado al job
  $query = "select jobData.nameDoc from jobData where jobData.idjobData = $jobID";
  $resultado = mysqli_query($conexion, $query);
  $nameDoc = mysqli_fetch_assoc($resultado)['nameDoc'];

  #data set training
  $training = "/var/www/html/MLSTrainingTool/jobs/".$jobID."/".$nameDoc;
  $newDataSet = "/var/www/html/MLSTrainingTool/jobs/".$jobID."/".$nameDocument;
  $pathResponse = "/var/www/html/MLSTrainingTool/jobs/".$jobID."/";
  $metaModels = "/var/www/html/MLSTrainingTool/jobs/".$jobID."/meta_models.json";

  #formamos el comando python para hacer la ejecucion correspondiente
  $command = "python /var/www/html/MLSTrainingTool/models/bin/tryUseModelsPrediction.py ".$training." ".$newDataSet." ".$metaModels." ".$pathResponse;
  $output = [];

  exec($command, $output);
  $response['exec'] = $output[0];

  echo json_encode($response);

?>
