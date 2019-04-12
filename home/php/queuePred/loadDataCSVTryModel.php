<?php

  /*
    script que permite cargar un archivo csv y leerlo para cargar la respuesta en formato JSON y
    exportarla al documento...
  */
  $job = $_REQUEST['job'];

  $nameDocument = "/var/www/html/MLSTrainingTool/jobs/$job/resultResponseExamples.csv";
  $row = 0;

  $matrixResponse = [];
  $header = ['Example', 'Average', 'StandarDeviation', 'MaxValue', 'MinValue', 'Range'];
  $dataAdd = 0;
  $index=0;
  #mean,std,max,min
  if (($handle = fopen($nameDocument, "r")) !== FALSE) {
    while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
      $rowData= [];
      $num = count($data);
      if ($row != 0){
        $rowData['Example'] = $index;
        for ($c=0; $c < $num; $c++) {

            $rowData[$header[$c+1]] = $data[$c];
        }

        #agregamos el valor del rango
        $rangemenos = $data[0]-$data[1];
        $rangemas = $data[0] + $data[1];
        $range = "[$rangemenos : $rangemas]";
        $rowData['Range'] = $range;
        $matrixResponse[$dataAdd] = $rowData;
        $dataAdd++;
      }
      $row++;
      $index++;
    }
    fclose($handle);
  }

  $responseData['data'] = $matrixResponse;
  echo json_encode($responseData);
?>
