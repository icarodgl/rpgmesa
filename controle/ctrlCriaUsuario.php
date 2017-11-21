<html>
    <head>
      
        <meta charset="UTF-8">  
        <title>RPG Mesa</title>
        <script type="text/javascript" src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
        <!-- Compiled and minified CSS -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/css/materialize.min.css">
        <!-- Compiled and minified JavaScript -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.100.2/js/materialize.min.js"></script>

        <!--Import Google Icon Font-->
        <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
        <!--Import materialize.css-->   
        <!--Let browser know website is optimized for mobile-->
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <script type="text/javascript" src="js/materialize.min.js"></script>
        <!--Import Meu CSS--> 
        <link rel="stylesheet" href="../estaticos/estiloBase.css" >
    </head>
    <body>
<?php

require_once '../model/Classes/Usuario/Usuario.php';
require_once '../model/GenericDAO/DaoGenericaImp.php';

use model\GenericDAO\DaoGenericaImp as DaoGenericaImp;
use model\Classes\Usuario\Usuario as Usuario;

$nome = $_POST["nome"];
$email = $_POST["email"];
$senha = $_POST["senha"];
$usuario = new Usuario;
$dao = new DaoGenericaImp;
$usuario->setUsername($nome);
$usuario->setEmail($email);
$usuario->setDataCadastro(new DateTime("now"));
$usuario->setSenha($senha);
$dao->inserir($usuario);

echo 'Usuario salvo: '."<br>Nome: ".$usuario->getUsername() ."<br> ID: ". $usuario->getId() ."<br>Email: ". $usuario->getEmail();
?>
</body>