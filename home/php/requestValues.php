<?php

  session_start();
  $idUSer = $_SESSION['idUser'];

  $values['request'] = $idUSer;

  echo json_encode($values);

?>
