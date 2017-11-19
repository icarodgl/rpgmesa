<?php
require_once '../model/Classes/Acoes/Acoes.php';
require_once '../model/Classes/Personagem/Jogador.php';
require_once '../model/Classes/Personagem/NaoJogador.php';
require_once '../model/Classes/Item/Utilizavel.php';
/* teste de usuario
  require_once '../bootstrap.php';
  echo "Olá!<br>";
  $usuario = $entityManager->find('Usuario', 1);
  echo $usuario->getUsername();
  teste de usuario */


$acao = new Acoes();
$joao = new Jogador();
$gigante = new NaoJogador();
$pocao = new Utilizavel();

$pocao->setNome("Pocao de Cura Fraca");
$joao->setNome("João");
$gigante->setNome("Gigante");

$acao->InserirAcao("Procurar item no cenário");
$acao->InserirAcao($joao->atacar($gigante));
$acao->InserirAcao($gigante->atacar($joao));
$acao->InserirAcao($pocao->usar($joao));

$acao->finalizarHistoria();
?>