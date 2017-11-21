<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of FabricaAcao
 *
 * @author icaro
 */
class FabricaAcao {

    function geraAcao(string $tipoAcao) {
        $acao = NULL;

        switch ($tipoAcao) {
            case "ataque":
                $acao = new Atacar();

                break;
            case "interagir":

                $acao = new Interagir();
                break;

            case "trocacena":

                $acao = new TrocarCena();
                break;
            default:
                break;
        }
        return $acao;
    }

}
