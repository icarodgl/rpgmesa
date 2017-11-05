<?php
/**
 * @Entity */
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
