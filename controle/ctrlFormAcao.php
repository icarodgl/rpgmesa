<?php /*
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


$dor = $_POST["interador"]?? "interador";
$gido = $_POST["interagido"]?? "interagido";
$tipoAcao = $_POST["tipocacao"]?? "interacao";

$log = new LinhaDoTempo();
$fabrica = new FabricaAcao();
$dao = new DaoGenericaImp();
$per1 = new Jogador();
$per1->setNome($dor);
$per2 = new NaoJogador();
$per2->setNome($gido);

$acao = $fabrica->geraAcao($tipoAcao);
$act = "interagiu" ;//$acao->gerar($per1, $per2);
$log->getDescricao($act);

$log->setData(new DateTime("now"));
$log->setSucesso(1);
$dao->inserir($log);

$d = $log->getDescricao();
$t = $log->getData();
$s = $log->getSucesso();
echo "$act";
echo "$d $d : $s"; */
require_once '../bootstrap.php';
require_once '../model/GenericDAO/DaoGenerica.php';
require_once '../model/GenericDAO/DaoGenericaImp.php';

use model\GenericDAO\DaoGenerica;
use model\GenericDAO\DaoGenericaImp;

$dao = new DaoGenericaImp();

$dor = $_POST["interador"]?? "interador";
$gido = $_POST["interagido"]?? "interagido";
$tipoAcao = $_POST["tipocacao"]?? "interacao";



$pegadata = new DateTime('now');
$datastr = date_format($pegadata, 'y-m-d h:m:s');
$sucesso = rand( 0, 1);
$sql = "INSERT INTO `linhadotempo` (`IdLinhaDoTempo`, `IdPersonagem`, `IdPartida`, `Sucesso`, `Descricao`, `Data`) 
VALUES (NULL, '1', '3', '$sucesso', '"."$dor $tipoAcao $gido "."', '$datastr');";

if ($dao->setQuery($sql)) {
    echo "sucesso!";
    echo '<meta http-equiv="refresh" content=1;url="../views/index.php">';
} else {
    echo "Error: " . $sql . "<br>";
}



?>