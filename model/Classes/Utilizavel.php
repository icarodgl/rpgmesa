<?php
require_once 'Item.php';
/**
 * @Entity
 */
class Utilizavel  extends Item{
    
    /** @Column(type="integer", name="Tempo") */
    private $tempo;
   
    /** @Column(type="integer", name="Dano") */
    private $dano;
   
    /** @Column(type="integer", name="Cargas") */
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
