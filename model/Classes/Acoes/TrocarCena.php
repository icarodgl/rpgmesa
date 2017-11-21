<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of rocarCena
 *
 * @author icaro
 */
class TrocarCena implements Acao{

    public function gerar($interador, $interagido) {
        $a = $interador->getNome();
        $b = $interagido->getNome();
        $agora = date("d/m/y H:i:s");
        echo '<li class="collection-item">';
        echo "$agora : ";
        echo "$a troca a cena para: $b <br>";
        echo '</li>';
        return $descricao = "outra montanha!";
    }

}
