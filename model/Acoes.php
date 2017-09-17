<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of Acoes
 *
 * @author icaro
 */
class Acoes {
    private $sucesso;
    private $descricao;
    private $data;
    private $hora;
    
    function getSucesso() {
        return $this->sucesso;
    }

    function getDescricao() {
        return $this->descricao;
    }

    function getData() {
        return $this->data;
    }

    function getHora() {
        return $this->hora;
    }

    function setSucesso($sucesso) {
        $this->sucesso = $sucesso;
    }

    function setDescricao($descricao) {
        $this->descricao = $descricao;
    }

    function setData($data) {
        $this->data = $data;
    }

    function setHora($hora) {
        $this->hora = $hora;
    }


}
