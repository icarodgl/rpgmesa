<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of Atributos
 *
 * @author icaro
 */
class Atributos {
    private $forca;
    private $vigor;
    private $agilidade;
    private $intelcto;
    private $espirito;
    function getForca() {
        return $this->forca;
    }

    function getVigor() {
        return $this->vigor;
    }

    function getAgilidade() {
        return $this->agilidade;
    }

    function getIntelcto() {
        return $this->intelcto;
    }

    function getEspirito() {
        return $this->espirito;
    }

    function setForca($forca) {
        $this->forca = $forca;
    }

    function setVigor($vigor) {
        $this->vigor = $vigor;
    }

    function setAgilidade($agilidade) {
        $this->agilidade = $agilidade;
    }

    function setIntelcto($intelcto) {
        $this->intelcto = $intelcto;
    }

    function setEspirito($espirito) {
        $this->espirito = $espirito;
    }


}
