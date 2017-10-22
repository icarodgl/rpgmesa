<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author icaro
 */
interface DaoUsuario extends DaoGenerica{
    
public function buscarLoginSenha($login, $senha);
}
