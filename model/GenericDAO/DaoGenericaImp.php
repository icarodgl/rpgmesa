<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Description of DaoGenericaImp
 *
 * @author icaro
 */
use Doctrine\ORM\Tools\Setup;
use Doctrine\ORM\EntityManager;

require_once "vendor/autoload.php";


class DaoGenericaImp implements DaoGenerica {
    
private $isDevMode;
private $config;
    
function __construct() {
    $this->isDevMode = true;
    $this->config = Setup::createAnnotationMetadataConfiguration(array(__DIR__."model/Classes"), $isDevMode);
}

    public function alterar($objeto) {
        
    }

    public function deletar($objeto) {
        
    }

    public function inserir($objeto) {
        
    }

    public function listar($objeto) {
        
    }

    
}
