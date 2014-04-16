var integ = [
        {"name":"Lina Marcela Aguirre","twitter":"https://twitter.com/LinaAguirreG","class":"lina"},
        {"name":"Edwin Fernando Mesa.","twitter":"https://twitter.com/edwinfmesa","class":"edwinfmesa"},
        {"name":"Ana Maria Moreno","twitter":"https://twitter.com/morenoanita123","class":"ana"},
        {"name":"José Mauricio Aizaga","twitter":"https://twitter.com/MaoAiz","class":"maoaiz"}
    ];
var integ2=[];

function generarOrder(){
    integ2=generarArreglo(integ.length)
    members = {};
    for(i=0;i<integ.length;i++){
        members[i] = integ[integ2[i]]
    }
    var s = swig.render($("#member-template").html(), {locals: members});
    $("#team .member-team > .row").append(s).fadeIn(900);
}

function generarArreglo(n){
    for(i=0;i<n;i++){
        var al=aleatorio(0,n-1)
        if(integ2.indexOf(al)==-1){
            integ2[integ2.length]=al;
        }
        else{
            i--;
        }
    }
    return integ2;
}

function aleatorio(inferior,superior){ 
    numPosibilidades = superior - inferior;
    aleat = Math.random() * numPosibilidades;
    aleat = Math.round(aleat);
    return parseInt(inferior) + aleat;
}

function main(){
    generarOrder();
}

function goToByScroll(element, callback){
    $('html,body').animate({
        scrollTop: $(element).offset().top - 100},
        'slow', callback);
}
$(document).ready(generarOrder);