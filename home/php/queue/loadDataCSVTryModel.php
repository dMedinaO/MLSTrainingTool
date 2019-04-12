<?php

  /*
    script que permite cargar un archivo csv y leerlo para cargar la respuesta en formato JSON y
    exportarla al documento...
  */
  $job = $_REQUEST['job'];

  $nameDocument = "/var/www/html/MLSTrainingTool/jobs/$job/responseTryModel.csv";
  $row = 0;

  $matrixResponse = [];
  $header = ['Example', 'Class', 'Prob'];
  $dataAdd = 0;
  $index=0;
  #mean,std,max,min
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
