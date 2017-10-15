<?php

class Ficha {
    
    private $raca;
    private $classe;
    private $tendencia;
    private $idade;
    private $peso;
    private $altura;
    private $sexo;
    private $deslocamento;
    private $iniciativa;
    private $carga;
    private $cargaMax;
    private $atributos;
    private $pericias = [];
    
    
    function __construct() {
        
    }

    function getAtributos() {
        return $this->atributos;
    }

    function getPericias() {
        return $this->pericias;
    }

    function setAtributos($atributos) {
        $this->atributos = $atributos;
    }

    function setPericias($pericias) {
        $this->pericias = $pericias;
    }

    function getRaca() {
        return $this->raca;
    }

    function getClasse() {
        return $this->classe;
    }

    function getTendencia() {
        return $this->tendencia;
    }

    function getIdade() {
        return $this->idade;
    }

    function getPeso() {
        return $this->peso;
    }

    function getAltura() {
        return $this->altura;
    }

    function getSexo() {
        return $this->sexo;
    }

    function getDeslocamento() {
        return $this->deslocamento;
    }

    function getIniciativa() {
        return $this->iniciativa;
    }

    function getCarga() {
        return $this->carga;
    }

    function getCargaMax() {
        return $this->cargaMax;
    }

    function setRaca($raca) {
        $this->raca = $raca;
    }

    function setClasse($classe) {
        $this->classe = $classe;
    }

    function setTendencia($tendencia) {
        $this->tendencia = $tendencia;
    }

    function setIdade($idade) {
        $this->idade = $idade;
    }

    function setPeso($peso) {
        $this->peso = $peso;
    }

    function setAltura($altura) {
        $this->altura = $altura;
    }

    function setSexo($sexo) {
        $this->sexo = $sexo;
    }

    function setDeslocamento($deslocamento) {
        $this->deslocamento = $deslocamento;
    }

    function setIniciativa($iniciativa) {
        $this->iniciativa = $iniciativa;
    }

    function setCarga($carga) {
        $this->carga = $carga;
    }

    function setCargaMax($cargaMax) {
        $this->cargaMax = $cargaMax;
    }


}
