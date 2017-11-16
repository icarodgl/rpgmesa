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
interface DaoGenerica {
    function listar();
    function deletar($objeto);
    function alterar($objeto);
    function inserir($objeto);
}
