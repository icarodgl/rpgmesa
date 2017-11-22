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
        <div class="container">
            <div class="row">
                <form class="col s10" action="../controle/ctrlFormAcao.php" method="post">
                    <div class="row">
                        <div class="input-field col s5">
                            <input placeholder="nome do interador" id="first_name" type="text" class="validate" name="interador">
                            <label for="Nome">interador</label>
                        </div>
                    </div>
                    <div class="row">
                        <div class="input-field col s5">
                            <input placeholder="nome interador ou cena" id="first_name" type="text" class="validate" name="interagido">
                            <label for="Nome">interagido</label>
                        </div>
                    </div>
                    <div class="row">
                    <div class="input-field col s5">
                        <select name="tipocacao">
                            <option value="" disabled selected>escolha...</option>
                            <option value="ataque">Atacar!</option>
                            <option value="interagir">Interage</option>
                            <option value="trocacena">Troca Cena</option>
                        </select >
                        <label>ações</label>
                    </div>

</div>
<input type="submit" value="Jogar!">
            </div>
            
            </form>
        </div>
    </div>
</body>
<script>
$(document).ready(function() {
    $('select').material_select();
  });
</script>
</html>
