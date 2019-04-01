<?php

  /*
    script que permite cargar un archivo csv y leerlo para cargar la respuesta en formato JSON y
    exportarla al documento...
  */
  $job = $_REQUEST['job'];
  $nameFile = $_REQUEST['feature'];
  $nameDocument = "/var/www/html/MLSTrainingTool/jobs/$job/$nameFile.csv";
  $row = 0;

  $matrixResponse = [];
  $header = ['Algorithm', 'Params', 'Validation','Accuracy', 'Recall',	'Precision', 'F1Score'];
  $dataAdd = 0;

  if (($handle = fopen($nameDocument, "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
      $rowData= [];
      $num = count($data);
      if ($row != 0){
        for ($c=0; $c < $num; $c++) {

            $rowData[$header[$c]] = $data[$c];
        }
        $matrixResponse[$dataAdd] = $rowData;
        $dataAdd++;
      }
      $row++;
    }
    fclose($handle);
  }

  $responseData['data'] = $matrixResponse;
  echo json_encode($responseData);
?>
