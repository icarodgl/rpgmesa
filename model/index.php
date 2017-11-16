<!DOCTYPE html>

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

    <?php
    require_once 'Classes/Acoes/Acoes.php';
    require_once 'Classes/Personagem/Jogador.php';
    require_once 'Classes/Personagem/NaoJogador.php';
    /*teste de usuario*/
        require_once '../bootstrap.php';
        echo "Olá!<br>";
        $usuario = $entityManager->find('Usuario', 1);
        echo $usuario->getUsername();
   /*teste de usuario*/
    
    
    $acao = new Acoes();
    $joao = new Jogador();
    $gigante = new NaoJogador();
    
    $joao->setNome("João");
    $gigante->setNome("Gigante");
    
    $acao->InserirAcao("Procurar item no cenário");
    $acao->InserirAcao($joao->atacar($gigante));
    
    $acao->finalizarHistoria();
    
    ?>

</body>
</html>
