var varconf = setInterval(atualizador, 1000)

function atualizador() {
    pegaConteudo("../controle/ctrlLinhaDoTempo.php")
    
}


function pegaConteudo(conteudoHTML){
    $.ajax({
        url : conteudoHTML,
        cache: false,
        success : function(result){
            document.getElementById("linhadotempo").innerHTML = result
            
        }
    })
}