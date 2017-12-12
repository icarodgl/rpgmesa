<?php

require_once 'Item.php';
/**
 * @Entity
 */
class Armamento extends Item{
    
    /** @Column(type="integer", name="Dano") */
    private $dano;
    
    /** @Column(type="integer", name="Acerto") */
    private $acerto;
   
    /** @Column(type="integer", name="Mao") */
    private $mao;
   
    /** @Column(type="integer", name="TipoDado") */
    private $tipoDado;
   
    /** @Column(type="integer", name="QuatDado") */
    private $quatDado;
    
    
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
        return $this->quatDado;
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
        $this->quatDado = $quantDado;
    }


}
