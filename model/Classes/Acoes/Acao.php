<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of Acoes
 *
 * @author icaro
 */
 use Doctrine\ORM\Mapping as ORM;   

/**
 * @Entity 
 * @Table(name="users")
 */
interface Acao {
    
function gerar($interador, $interagido) ;
}
