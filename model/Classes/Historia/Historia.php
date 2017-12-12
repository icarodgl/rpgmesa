<?php
/**
 * @Entity
 * @Table(name="Historia")
 */
class Historia {
    
    /**
     * @Id @GeneratedValue 
     * @GeneratedValue("AUTO")
     * @Column(type="integer", name="IdHistoria")
     */
    private $idHistoria;
    
    /**
     * @ORM\Column(type="string", length=45, name="Nome")
     */
    private $nome;
    /**
     * @ORM\Column(type="string", length=45, name="Descricao")
     */
    private $descricao;
    /**
     * @ORM\Column(type="string", length=45, name="Capa")
     */
    private $capa;
    function getIdHistoria() {
        return $this->idHistoria;
    }

    function getNome() {
        return $this->nome;
    }

    function getDescricao() {
        return $this->descricao;
    }

    function getCapa() {
        return $this->capa;
    }

    function setIdHistoria($idHistoria) {
        $this->idHistoria = $idHistoria;
    }

    function setNome($nome) {
        $this->nome = $nome;
    }

    function setDescricao($descricao) {
        $this->descricao = $descricao;
    }

    function setCapa($capa) {
        $this->capa = $capa;
    }


}
