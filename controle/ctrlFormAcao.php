<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
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
require_once '../model/Classes/Acoes/Acao.php';
require_once '../model/Classes/Acoes/Atacar.php';
require_once '../model/Classes/Acoes/Interagir.php';
require_once '../model/Classes/Acoes/TrocarCena.php';
require_once '../model/FabricaAcao/FabricaAcao.php';
require_once '../model/Classes/Personagem/Jogador.php';
require_once '../model/Classes/Personagem/NaoJogador.php';
require_once '../model/Classes/Usuario/Usuario.php';
require_once '../model/Classes/LinhaDoTempo/LinhaDoTempo.php';
require_once '../model/GenericDAO/DaoGenericaImp.php';

use model\Classes\Acoes\FabricaAcao;
use model\Classes\Personagem\Jogador;
use model\Classes\Personagem\NaoJogador;
use model\GenericDAO\DaoGenericaImp as DaoGenericaImp;


$dor = $_POST["interador"];
$gido = $_POST["interagido"];
$tipoAcao = $_POST["tipocacao"];

$log = new LinhaDoTempo();
$fabrica = new FabricaAcao();
$dao = new DaoGenericaImp();
$per1 = new Jogador();
$per1->setNome($dor);
$per2 = new NaoJogador();
$per2->setNome($gido);

$acao = $fabrica->geraAcao($tipoAcao);
$act = $acao->gerar($per1, $per2);
$log->getDescricao($act);

$log->setData(new DateTime("now"));
$log->setSucesso(rand(0, 1));
$dao->inserir($log);

$d = $log->getDescricao();
$t = $log->getData();
$s = $log->getSucesso();
echo "$act";
echo "$d $d : $s";
?>
    </body>
</html>
