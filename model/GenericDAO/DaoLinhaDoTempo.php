<?php

class DaoLinhaDoTempo extends \model\GenericDAO\DaoGenericaImp{
    
    
    function salvarLinhadoTempo(LinhaDoTempo $lt){
        
        $pegadata = new DateTime('now');
        $datastr = date_format($pegadata, 'y-m-d h:m:s');
        
        $sql = "INSERT INTO `linhadotempo` (`IdLinhaDoTempo`, `IdPersonagem`, `IdPartida`, `Sucesso`, `Descricao`, `Data`) 
        VALUES (NULL, '".$lt->getPersonagem()."', '".$lt->getPartida()."', '".$lt->getSucesso()."', '".$lt->getDescricao()."', '$datastr');";
        
        
    }
}