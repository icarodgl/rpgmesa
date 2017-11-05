<?php
/**
 * @Entity
 */
class Atributo {
    /**
    * @Id
    * @Column(type="integer", name="IdAtributo")
    * @GeneratedValue(strategy="AUTO")*/
    protected $id;
    
    /** @Column(type="integer", name="Forca") */
    private $forca;
    /** @Column(type="integer", name="Vigor") */
    private $vigor;
    /** @Column(type="integer", name="Agiliade") */
    private $agilidade;
    /** @Column(type="integer", name="Intelecto") */
    private $intelecto;
    /** @Column(type="integer", name="Espirito") */
    private $espirito;
    
    
    function getForca() {
        return $this->forca;
    }

    function getVigor() {
        return $this->vigor;
    }

    function getAgilidade() {
        return $this->agilidade;
    }

    function getIntelecto() {
        return $this->$intelecto;
    }

    function getEspirito() {
        return $this->espirito;
    }

    function setForca($forca) {
        $this->forca = $forca;
    }

    function setVigor($vigor) {
        $this->vigor = $vigor;
    }

    function setAgilidade($agilidade) {
        $this->agilidade = $agilidade;
    }

    function setIntelecto($intelecto) {
        $this->$intelecto = $intelecto;
    }

    function setEspirito($espirito) {
        $this->espirito = $espirito;
    }
}
