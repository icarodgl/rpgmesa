<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of LinhaDoTempo
 *
 * @author icaro
 */
class LinhaDoTempo {

    /**
     * @Id @GeneratedValue 
     * @GeneratedValue("AUTO")
     * @Column(type="integer")
     */
    private $id;

    /**
     * @ORM\Column(type="string", length=10)
     */
    private $sucesso;

    /**
     * @ORM\Column(type="string", length=200)
     */
    private $descricao;

    /**
     * @ORM\Column(type="string", length=20)
     */
    private $data;
    

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

    function InserirAcao(String $descricao) {
        $this->descricao = $descricao;
        $this->data = date("d/m/y H:i:s");
        $this->sucesso = TRUE;
        $this->atualizar();
    }

    function finalizarHistoria() {

        $this->descricao = "E viveram felizes para sempre";
        $this->data = date("d/m/y H:i:s");
        $this->sucesso = TRUE;
        $this->atualizar();
    }

    function atualizar() {
        echo '<li class="collection-item">';
        echo $this->data;
        echo ' : ';
        echo $this->descricao;
        echo ' : ';

        if ($this->sucesso) {
            echo 'Sucesso!';
        } else {
            echo 'Falhou!   ';
        }
        echo '</li>';
    }

}
