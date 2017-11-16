<?php
/**
 * Personagem
 * 
 * @Entity
 * @Table(name="Personagem")
 */
class Personagem {

     /**
     * @Id
     * @Column(type="integer", name="IdPersonagem")
     * @GeneratedValue(strategy="AUTO")
     */
    protected $id;
    
    /**
     * @ManyToOne(targetEntity="Usuario")
     * @JoinColumn(name="IdUsuario", referencedColumnName="IdUsuario")
     */
    protected $usuario;
    
    /**
     * @Column(type="string", name="Nome")
     */
    protected $nome;
    
    /**
     * @Column(type="integer", name="Experiencia")
     */
    protected $experiencia;
    
    /**
     * @Column(type="integer", name="Level")
     */
    protected $level;
    
    /**
     * @Column(type="integer", name="Saude")
     */
    protected $saude;
    
    /**
     * @Column(type="string", name="Imagem")
     */
    protected $imagem;    

    
    function getNome() {
        return $this->nome;
    }

    function getImagem() {
        return $this->imagem;
    }

    function getExperiencia() {
        return $this->experiencia;
    }

    function getLevel() {
        return $this->level;
    }

    function getSaude() {
        return $this->saude;
    }

    function setNome($nome) {
        $this->nome = $nome;
    }

    function setImagem($imagem) {
        $this->imagem = $imagem;
    }

    function setExperiencia($experiencia) {
        $this->experiencia = $experiencia;
    }

    function setLevel($level) {
        $this->level = $level;
    }

    function setSaude($saude) {
        $this->saude = $saude;
    }


    function atacar(Personagem $personagem){
        $descricao = $this->nome . " Atacou " . $personagem->getNome();
        return $descricao;
    }
    function acao(){}
    function testePericia(){}

}
