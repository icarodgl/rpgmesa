<?php

use 'model\Classes\Personagem\Jogador';

class PartidaDedBuilder extends BuilderPartida{
    
    private $nomeJogo;
    private $mestre; 
    private $historia;
    private $jogadores;
    private $partida;
    
    function __construct() {
        $this->mestre = new Jogador();
        $this->jogadores = Array();
        $this->historia = new Historia();
        $this->partida = new Partida();
    }

    public function ConstruirPartidaDed($jogadores, $mestre, $historia, $nomeJogo){
        $this->nomeJogo = $nomeJogo;
        $this->jogadores = $jogadores;
        $this->mestre = $mestre;
        $this->historia = $historia;
    }
    
    function criarPartida(){
        $this->partida->setNomeJogo($this->nomeJogo);
    }
    
    function associaMestre(){
        $this->partida->setMestre($this->mestre);
    }
    function associaJogadores(){
        $participante = new Participante();
        $participante->setPartida($this->partida);
        
        foreach ($this->jogadores as $jogador) {
            $participante->setIdparticipante(0);
            $participante->setPersonagem($jogador);
            $participante->setUsuario($jogadores->getUsuario);
        }   
    }
    
    function associaJogo(){
        $this->partida->setHistoria($this->historia);
    }
    
}
