<?php
/**
 * @Entity
 * @Table(name="Participante")
 */
class Participante {
    
    /**
     * @Id @GeneratedValue 
     * @GeneratedValue("AUTO")
     * @Column(type="integer", name="IdParticipante")
     */
    private $idparticipante;
    
    /**
     * @ManyToOne(targetEntity="Partida")
     * @JoinColumn(name="IdPartida", referencedColumnName="IdPartida")
     */
    protected $partida;
    
    /**
     * @ManyToOne(targetEntity="Personagem")
     * @JoinColumn(name="IdPersonagem", referencedColumnName="IdPersonagem")
     */
    protected $personagem;
    
    /**
     * @ManyToOne(targetEntity="Usuario")
     * @JoinColumn(name="IdUsuario", referencedColumnName="IdUsuario")
     */
    protected $usuario;
    function getIdparticipante() {
        return $this->idparticipante;
    }

    function getPartida() {
        return $this->partida;
    }

    function getPersonagem() {
        return $this->personagem;
    }

    function getUsuario() {
        return $this->usuario;
    }

    function setIdparticipante($idparticipante) {
        $this->idparticipante = $idparticipante;
    }

    function setPartida($partida) {
        $this->partida = $partida;
    }

    function setPersonagem($personagem) {
        $this->personagem = $personagem;
    }

    function setUsuario($usuario) {
        $this->usuario = $usuario;
    }


}