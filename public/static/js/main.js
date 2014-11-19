var integ = [
        {"name":"Lina Marcela Aguirre", "class":"lina", "job": "Directora administrativa", "social": {"twitter": {"url": "https://twitter.com/LinaAguirreG", "username": "LinaAguirreG"}}},
        {"name":"Edwin Fernando Mesa", "class":"edwinfmesa", "job": "Director de estrategias", "social": {"twitter": {"url": "https://twitter.com/edwinfmesa", "username": "edwinfmesa"}}},
        {"name":"Ana Maria Moreno", "class":"ana", "job": "Directora de arte y diseño", "social": {"twitter": {"url": "https://twitter.com/morenoanita123", "username": "morenoanita123"}}},
        {"name":"José Mauricio Aizaga", "class":"maoaiz", "job": "Director de tecnología", "social": {"twitter": {"url": "https://twitter.com/MaoAiz", "username": "MaoAiz"}}}
    ];
var integ2=[];

function ordering(){
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
    ordering();
    $("#daiech-menu ul.nav li a[href^='/#'], a[href='#projects']").on('click', function(e) {
        e.preventDefault();
        goToByScroll(this.hash, function (e) {});
    });
}

function goToByScroll(element, callback){
    $('html,body').animate({
        scrollTop: $(element).offset().top - 10},
        'slow', callback);
}
$(document).ready(main);
$("#language-form button").on("click", function (e){e.preventDefault();$("#language-selected").val($(this).attr("data-language"));$("#language-form").submit();})