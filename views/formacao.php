
<div class="row">
    <div class="col s4"></div>
    <form class="col s8" action="../controle/ctrlFormAcao.php" method="post">
        <div class="row">
            <div class="input-field col s5">
                <input placeholder="nome do interador" id="first_name" type="text" class="validate" name="interador">
                <label for="Nome">Interador</label>
            </div>
        </div>
        <div class="row">
            <div class="input-field col s5">
                <input placeholder="nome interador ou cena" id="first_name" type="text" class="validate" name="interagido">
                <label for="Nome">Interagido</label>
            </div>
        </div>
        <div class="row">
        <div class="col s5">
        <label>Ações</label>
            <select class="browser-default" name="tipocacao">
                <option value="" disabled selected>Ações...</option>
                <option value="ataque">Atacar!</option>
                <option value="interagir">Interage</option>
                <option value="trocacena">Troca Cena</option>
            </select >
            
        </div>

</div>
<input type="submit" value="Jogar!">
</div>
            </form>
<script>
$(document).ready(function() {
    $('select').material_select();
  });
</script>
