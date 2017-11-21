<?php
namespace model\Classes\Acoes;
use model\Classes\Acoes\Acao;
require_once 'Acao.php';
/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of Interagir
 *
 * @author icaro
 */

class Interagir implements Acao{

    public function gerar($interador, $interagido) {
        $a = $interador->getNome();
        $b = $interagido->getNome();
        $agora = date("d/m/y H:i:s");
        echo '<li class="collection-item">';
        echo "$agora : ";
        echo "$a interage com  $b<br>";
        echo '</li>';
        return $descricao = "cutucar!";
    }

}
