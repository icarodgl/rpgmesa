<?php
/**
 * @Entity
 * @Table(name="Ficha")
 */
class Ficha {
    /**
     * @Id
     * @Column(type="integer", name="IdFicha")
     * @GeneratedValue(strategy="AUTO")
     */
    protected $id;
    /**
     * @ManyToOne(targetEntity="Personagem")
     * @JoinColumn(name="IdPersonagem", referencedColumnName="IdPersonagem")
     */
    //protected $personagem;
    /** @Column(type="string", name="Raca") */
    private $raca;
    /** @Column(type="string", name="Classe") */
    private $classe;
    /** @Column(type="string", name="Tendencia") */
    private $tendencia;
    /** @Column(type="integer", name="Idade") */
    private $idade;
    /** @Column(type="integer", name="Peso") */
    private $peso;
    /** @Column(type="integer", name="Altura") */
    private $altura;
    private $sexo;
    /** @Column(type="string", name="Deslocamento") */
    private $deslocamento;
    /** @Column(type="integer", name="Iniciativa") */
    private $iniciativa;
    /** @Column(type="integer", name="CargaMax") */
    private $cargaMax;
    
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

    function setCargaMax($cargaMax) {
        $this->cargaMax = $cargaMax;
    }
}
