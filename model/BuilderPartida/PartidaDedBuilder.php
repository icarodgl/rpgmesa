<?php

use 'model\Classes\Personagem\Jogador';
use 'model\GenericDAO\DaoGenericaImp';

class PartidaDedBuilder extends BuilderPartida{
    
    private $partida;
    private $dao;
    
    function __construct() {
        $this->mestre = new Jogador();
        $this->jogadores = Array();
        $this->historia = new Historia();
        $this->partida = new Partida();
        $this->dao = new DaoGenericaImp();
    }

    function criarPartida(){
        $this->partida->setIdPartida(0);
        $this->partida->setNomeJogo($this->nomeJogo);
        $this->dao->inserir($this->partida);
    }
    
    function associaMestre($mestre){
        $this->partida->setMestre($mestre);
        $this->dao->alterar($this->partida);
    }
    function associaJogadores($jogadores){
        $participante = new Participante();
        $participante->setPartida($this->partida);
        
        foreach ($jogadores as $jogador) {
            $participante->setIdparticipante(0);
            $participante->setPersonagem($jogador);
            $participante->setUsuario($jogadores->getUsuario);
            $this->dao->inserir($participante);
        }   
    }
    
    function associaJogo($historia){
        $this->partida->setHistoria($historia);
        $this->dao->alterar($this->partida);
    }
    
}
