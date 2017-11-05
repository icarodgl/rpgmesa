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
    
    
    
}
