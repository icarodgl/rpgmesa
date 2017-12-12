<?php
require_once 'Item.php';
/**
 * @Entity
 */
class Armadura extends Item{
    
    
    
    /** @Column(type="integer", name="Defesa") */
    private $defesa;
   
    /** @Column(type="integer", name="Agilidade") */
    private $agilidade;
   
    /** @Column(type="integer", name="Arcano") */
    private $arcano;
    
    function getDefesa() {
        return $this->defesa;
    }

    function getAgilidade() {
        return $this->agilidade;
    }

    function getArcano() {
        return $this->arcano;
    }

    function setDefesa($defesa) {
        $this->defesa = $defesa;
    }

    function setAgilidade($agilidade) {
        $this->agilidade = $agilidade;
    }

    function setArcano($arcano) {
        $this->arcano = $arcano;
    }
}
