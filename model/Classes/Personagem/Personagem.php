<?php

class Personagem {
    private $nome;
    private $imagem;
    private $experiencia;
    private $level;
    private $saude;
    
    function getNome() {
        return $this->nome;
    }

    function getImagem() {
        return $this->imagem;
    }

    function getExperiencia() {
        return $this->experiencia;
    }

    function getLevel() {
        return $this->level;
    }

    function getSaude() {
        return $this->saude;
    }

    function setNome($nome) {
        $this->nome = $nome;
    }

    function setImagem($imagem) {
        $this->imagem = $imagem;
    }

    function setExperiencia($experiencia) {
        $this->experiencia = $experiencia;
    }

    function setLevel($level) {
        $this->level = $level;
    }

    function setSaude($saude) {
        $this->saude = $saude;
    }


    function atacar(Personagem $personagem){
        $descricao = $this->nome . " Atacou " . $personagem->nome;
        return $descricao;
    }
    function acao(){}
    function testePericia(){}
}
