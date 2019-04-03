<?php

	header('Content-Type: application/json');

	$idjob = $_REQUEST['job'];

	#eliminamos el directorio
	$output1 = [];
	$output2 = [];
	$output3 = [];
	$output4 = [];

	$command1 = "cat /var/www/html/MLSTrainingTool/jobs/$idjob/Accuracy.csv | wc -l";
	$command2 = "cat /var/www/html/MLSTrainingTool/jobs/$idjob/Precision.csv | wc -l";
	$command3 = "cat /var/www/html/MLSTrainingTool/jobs/$idjob/Recall.csv | wc -l";
	$command4 = "cat /var/www/html/MLSTrainingTool/jobs/$idjob/F1.csv | wc -l";

	exec($command1, $output1);
	exec($command2, $output2);
	exec($command3, $output3);
	exec($command4, $output4);

	//formamos el arreglo asociativo con la respuesta
	$response = [];
	$data1["performance"] = "Accuracy";
	$data1["value"] = $output1[0];

	$data2["performance"] = "Precision";
	$data2["value"] = $output2[0];

	$data3["performance"] = "Recall";
	$data3["value"] = $output3[0];

	$data4["performance"] = "F1";
	$data4["value"] = $output4[0];

	$response[0] = $data1;
	$response[1] = $data2;
	$response[2] = $data3;
	$response[3] = $data4;

	echo json_encode($response);
	
?>
