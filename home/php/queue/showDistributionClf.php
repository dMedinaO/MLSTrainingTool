<?php

	$idjob = $_REQUEST['job'];

	#eliminamos el directorio
	$output = [];
	$command = "python /var/www/html/MLSTrainingTool/models/bin/getSummaryModelsClf.py $idjob";
	exec($command, $output);

	echo json_encode($output[0]);
?>
