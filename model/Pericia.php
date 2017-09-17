<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of Pericia
 *
 * @author icaro
 */
class Pericia {
    
    private $nome;
    private $atributo;
    private $nivel;
    
    function getNome() {
        return $this->nome;
    }

    function getAtributo() {
        return $this->atributo;
    }

    function getNivel() {
        return $this->nivel;
    }

    function setNome($nome) {
        $this->nome = $nome;
    }

    function setAtributo($atributo) {
        $this->atributo = $atributo;
    }

    function setNivel($nivel) {
        $this->nivel = $nivel;
    }


}
