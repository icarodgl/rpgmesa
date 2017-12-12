<?php

class DiretorPartida{
    
    function ConstruirPatidaVampiro(){
    
    }
    
    function ConstruirPatidaDeD($jogadores, $mestre, $historia, $nomeJogo){
        $partida = new Partida();
        
        $partidaDedBuilder = new PartidaDedBuilder($partida);
        
        $partidaDedBuilder->criarPartida($nomeJogo);
        
        $partidaDedBuilder->associaJogo($historia);
        
        $partidaDedBuilder->associaMestre($mestre);
        
        $partidaDedBuilder->associaJogadores($jogadores);
    
    }
}




