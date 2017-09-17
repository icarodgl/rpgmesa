<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of Mapa
 *
 * @author icaro
 */
class Mapa {
    private $nome;
    private $imagem;
    private $cenarios = [];
            
    function getCenarios() {
        return $this->cenarios;
    }

    function setCenarios($cenarios) {
        $this->cenarios = $cenarios;
    }

        function getNome() {
        return $this->nome;
    }

    function getImagem() {
        return $this->imagem;
    }

    function setNome($nome) {
        $this->nome = $nome;
    }

    function setImagem($imagem) {
        $this->imagem = $imagem;
    }


}
