<?php

require_once 'Item.php';
class Armamento extends Item{
    private $dano;
    private $acerto;
    private $mao;
    private $tipoDado;
    private $quantDado;
    
    function getDano() {
        return $this->dano;
    }

    function getAcerto() {
        return $this->acerto;
    }

    function getMao() {
        return $this->mao;
    }

    function getTipoDado() {
        return $this->tipoDado;
    }

    function getQuantDado() {
        return $this->quantDado;
    }

    function setDano($dano) {
        $this->dano = $dano;
    }

    function setAcerto($acerto) {
        $this->acerto = $acerto;
    }

    function setMao($mao) {
        $this->mao = $mao;
    }

    function setTipoDado($tipoDado) {
        $this->tipoDado = $tipoDado;
    }

    function setQuantDado($quantDado) {
        $this->quantDado = $quantDado;
    }


}
