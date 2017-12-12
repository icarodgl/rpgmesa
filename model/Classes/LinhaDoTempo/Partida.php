<?php
/**
 * @Entity
 * @Table(name="Partida")
 */
class Partida {
    
    /**
     * @Id @GeneratedValue 
     * @GeneratedValue("AUTO")
     * @Column(type="integer", name="IdPartida")
     */
    private $idPartida;
    
    /**
     * @OneToMany(targetEntity="Historia")
     * @JoinColumn(name="IdHistoria", referencedColumnName="IdHistoria")
     */
    protected $historia;
    
    /**
     * @OneToMany(targetEntity="Usuario")
     * @JoinColumn(name="IdUsuario", referencedColumnName="IdMestre")
     */
    protected $mestre;
    
    /**
     * @ORM\Column(type="string", length=100, name="NomeJogo")
     */
    private $nomeJogo;

    function getIdPartida() {
        return $this->idPartida;
    }

    function getHistoria() {
        return $this->historia;
    }

    function getNomeJogo() {
        return $this->nomeJogo;
    }

    function setIdPartida($idPartida) {
        $this->idPartida = $idPartida;
    }

    function setHistoria($historia) {
        $this->historia = $historia;
    }

    function setNomeJogo($nomeJogo) {
        $this->nomeJogo = $nomeJogo;
    }

    function getMestre() {
        return $this->mestre;
    }

    function setMestre($mestre) {
        $this->mestre = $mestre;
    }
    
    


}