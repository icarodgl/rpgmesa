<?php

require_once 'Item.php';
class Armadura extends Item{
    private $defesa;
    private $agilidade;
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
