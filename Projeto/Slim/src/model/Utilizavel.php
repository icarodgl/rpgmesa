<?php
require_once 'Item.php';
class Utilizavel  extends Item{
    private $tempo;
    private $dano;
    private $cargas;
    
    
    function getTempo() {
        return $this->tempo;
    }

    function getDano() {
        return $this->dano;
    }

    function getCargas() {
        return $this->cargas;
    }

    function setTempo($tempo) {
        $this->tempo = $tempo;
    }

    function setDano($dano) {
        $this->dano = $dano;
    }

    function setCargas($cargas) {
        $this->cargas = $cargas;
    }
    

  
}
