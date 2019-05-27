<?php

	#script para hacer la carga de informacion desde la base de datos a la tabla
	include("../connection.php");

	$job = $_REQUEST['job'];
	$feature = $_REQUEST['feature'];

	$query = "select jobData.nameDoc as name from jobData where jobData.idjobData = $job";
	$resultado = mysqli_query($conexion, $query);

	$nameData = "";
	if (!$resultado){
		die("Error");
	}else{

		while($data = mysqli_fetch_assoc($resultado)){

			$nameData = $data['name'];
		}
	}

	//hacemos la ejecucion...
	$output = [];

	$dataSet = "/var/www/html/MLSTrainingTool/jobs/$job/$nameData";
	$command = "python /var/www/html/MLSTrainingTool/models/bin/evaluateShapiro.py $dataSet $feature";
	exec($command, $output);
	echo $output[0];

	mysqli_free_result($resultado);
	mysqli_close($conexion);
?>
