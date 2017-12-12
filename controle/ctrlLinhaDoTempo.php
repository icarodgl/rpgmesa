<?php

    // você já sabe o motivo deste require
    require_once '../bootstrap.php';
    
    require_once '../model/GenericDAO/DaoGenerica.php';
    require_once '../model/Classes/Usuario/Usuario.php';
    require_once '../model/Classes/Personagem/Personagem.php';
    require_once '../model/Classes/LinhaDoTempo/LinhaDoTempo.php';
    require_once '../model/GenericDAO/DaoGenericaImp.php';

    use model\Classes\Personagem\Personagem;
    use model\GenericDAO\DaoGenerica;
    use model\GenericDAO\DaoGenericaImp as DaoGenericaImp;
    use Doctrine\DBAL\Logging\EchoSQLLogger;

    $DaoGenericaImp = new DaoGenericaImp();
    $linhaTempo = new LinhaDoTempo();
    
    $DaoGenericaImp->getEntityManager();
    
    $sql = "SELECT * FROM LinhaDoTempo";
    
    $historicos = $DaoGenericaImp->getResult($sql);
  
    foreach ($historicos as $value) {
        if ($value['Sucesso']) {
            $sucesso = "sim";
        } else {
            $sucesso = "não";
        }
        echo '<li class="collection-item">';
        echo $value['Data']."<br>".$value['Descricao']."<br>Sucesso: ". $sucesso ." <br>";
        echo '</li>';
    }
    
    
    
?>