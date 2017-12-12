<?php


use model\Classes\Personagem\Personagem;
//use model\Classes\Partida\Personagem;

/**
 * @Entity
 * @Table(name="LinhaDoTempo")
 */
class LinhaDoTempo {
    
    /**
     * @Id @GeneratedValue 
     * @GeneratedValue("AUTO")
     * @Column(type="integer", name="IdLinhaDoTempo")
     */
    private $IdLinhaDoTempo;

    /**
     * @ORM\Column(type="string", length=10, name="Sucesso")
     */
    private $sucesso;

    /**
     * @ORM\Column(type="string", length=200, name="Descricao")
     */
    private $descricao;

    /**
     * @ORM\Column(type="DATETIME", length=20, name="Data")
     */
    private $data;
    
    function getId(){
        return $this->IdLinhaDoTempo;
    }
    
    /**
     * @ManyToOne(targetEntity="Personagem")
     * @JoinColumn(name="IdPersonagem", referencedColumnName="IdPersonagem")
     */
    protected $personagem;
     
    /**
     * @ManyToOne(targetEntity="Partida")
     * @JoinColumn(name="IdPartida", referencedColumnName="IdPartida")
     */
    //protected $partida;
    
    function getSucesso() {
        return $this->sucesso;
    }

    function getDescricao() {
        return $this->descricao;
    }

    function getData() {
        return $this->data;
    }

    function setId($id) {
        $this->IdLinhaDoTempo = $id;
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
        function getPersonagem() {
        return $this->personagem;
    }

    function getPartida() {
        return $this->partida;
    }

    function setPersonagem($personagem) {
        $this->personagem = $personagem;
    }

    function setPartida($partida) {
        $this->partida = $partida;
    }
}