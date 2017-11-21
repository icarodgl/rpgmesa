<?php
require_once '../model/Classes/Acoes/Acao.php';
require_once '../model/Classes/Acoes/Atacar.php';
require_once '../model/Classes/Acoes/Interagir.php';
require_once '../model/Classes/Acoes/TrocarCena.php';
require_once '../model/FabricaAcao/FabricaAcao.php';
require_once '../model/Classes/Personagem/Jogador.php';
require_once '../model/Classes/Personagem/NaoJogador.php';
require_once '../model/Classes/Item/Utilizavel.php';
require_once '../model/Classes/Usuario/Usuario.php';


/* teste de usuario
  require_once '../bootstrap.php';
  echo "Olá!<br>";
  $usuario = $entityManager->find('Usuario', 1);
  echo $usuario->getUsername();
 teste de usuario */

$fabrica = new FabricaAcao();
$acao;
$interador = new Jogador();
$interagido = new NaoJogador();
$interador->setNome("João");
$interagido->setNome("alguem");


$acao = $fabrica->geraAcao("ataque");

$acao->gerar($interador, $interagido);

$acao = $fabrica->geraAcao("interagir");

$acao->gerar($interador, $interagido);

$acao = $fabrica->geraAcao("trocacena");

$interagido->setNome("Castelo");
$acao->gerar($interador, $interagido);
?>