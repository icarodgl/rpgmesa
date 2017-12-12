
function gopegapartidas() {
    console.log('partidas')
    $.ajax({
        url: "./partidas.php",
        cache: false,
        success: function (result) {
            document.getElementById("corpo").innerHTML = result

        }
    })
}
function gocriador() {
    console.log('criador')
    $.ajax({
        url: "./formacao.php",
        cache: false,
        success: function (result) {
            document.getElementById("corpo").innerHTML = result

        }
    })
}
function gohome() {
    console.log('principal')
    $.ajax({
        url: "./principal.php",
        cache: false,
        success: function (result) {
            document.getElementById("corpo").innerHTML = result

        }
    })
}


window.onload = function () {
    document.getElementById("sidehome").addEventListener("click",function(){
        gohome()
    } )
    document.getElementById("sidepartidas").addEventListener("click",function(){
        gopegapartidas()
    } )

    document.getElementById("sidecriador").addEventListener("click",function(){
        gocriador()
    } )
    
}