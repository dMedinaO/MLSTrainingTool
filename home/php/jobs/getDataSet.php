<?php

	#script para hacer la carga de informacion desde la base de datos a la tabla
	include ("../connection.php");

	$job = $_REQUEST['job'];

	$query = "select jobData.nameDoc as name from jobData where jobData.idjobData = $job";
	$resultado = mysqli_query($conexion, $query);

	$nameData = "";
	if (!$resultado){
		die("Error");
	}else{

		while($data = mysqli_fetch_assoc($resultado)){

			$nameData = $data['name'];
		}
		$response['nameFile'] = $nameData;
		echo json_encode($response);

	}

	mysqli_free_result($resultado);
	mysqli_close($conexion);
?>
