<!DOCTYPE html>

<html>

    <head>
    <style>

    #cenario {
	position:absolute;
        top:10%;
	left:5%;
	max-width:600px;
        max-height:600px;
        width: auto;
        height: auto;
        z-index: -1;
	}
    #inimigo {
	position:relative;
        top: 150px;
        left: 30%;
        max-width:200px;
        max-height:200px;
        width: auto;
        height: auto;
	}
     </style>
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
    </head>

    <body>
        <nav>
            <div class="nav-wrapper">
                <a href="#" class="brand-logo">Logo</a>
                <ul id="nav-mobile" class="right hide-on-med-and-down">
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Partidas</a></li>
                    <li><a href="#">Histórias</a></li>
                </ul>
            </div>
        </nav>
        <div class="row">
            <div class="col s7">
                <img src="Imagens/castelo1.jpg" id="cenario" alt="Castelo" > 
                <img src="Imagens/guerreiro.png" id="inimigo" alt="inimigo" > 
                <img src="Imagens/guerreiro.png" id="inimigo" alt="inimigo" >  
            </div>
            <div class="col s5">
                
    <ul class="collection"  >
    <?php
    require_once 'Classes/Acoes/Acoes.php';
    require_once 'Classes/Personagem/Jogador.php';
    require_once 'Classes/Personagem/NaoJogador.php';
    require_once 'Classes/Item/Utilizavel.php';
    /*teste de usuario
        require_once '../bootstrap.php';
        echo "Olá!<br>";
        $usuario = $entityManager->find('Usuario', 1);
        echo $usuario->getUsername();
   teste de usuario*/
    
    
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
    </ul>
    </div>
    </div>
</body>
</html>
