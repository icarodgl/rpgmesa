
<?php

use Doctrine\DBAL\Logging\EchoSQLLogger;
require_once '../bootstrap.php';
require_once '../model/GenericDAO/DaoGenericaImp.php';
require_once '../model/GenericDAO/DaoGenerica.php';
use model\GenericDAO\DaoGenericaImp;

$dao = new DaoGenericaImp();

$result = $dao->getResult("SELECT * FROM partida");

    if (!is_null($result)){
        while($row = $result->fetch_assoc()) {
            echo '<li class="collection-item">';
            echo 'Nome : ' . $row['NomeJogo'] ; 
            echo '</li>';
        }
    } else{
        echo 'Nenhuma partida cadastrada';
    }
?> 