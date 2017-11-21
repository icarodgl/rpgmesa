<?php
/**
 * @Entity */
class Pericia {
         /**
     * @Id
     * @Column(type="integer", name="IdPericia")
     * @GeneratedValue(strategy="AUTO")
     */
    protected $id;
    /**
     * @Column(type="string", name="Nome")
     */
    private $nome;
        /**
     * @Column(type="integer", name="Atributo")
     */
    private $atributo;
    /**
     * @Column(type="integer", name="nivel")
     */
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
