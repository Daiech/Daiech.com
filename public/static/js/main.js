$(document).ready(main);
var integ = [
        {"nombre":"Lina","twitter":"https://twitter.com/LinaAguirreG","tw-pic":"https://si0.twimg.com/profile_images/1435962497/Imagen0725_bigger.jpg"},
        {"nombre":"Edwin","twitter":"https://twitter.com/edwinfmesa","tw-pic":"https://si0.twimg.com/profile_images/2227607157/foto_portada_bigger.jpg"},
        {"nombre":"Ana Maria","twitter":"https://twitter.com/morenoanita123","tw-pic":"https://si0.twimg.com/profile_images/1850492054/IMG_1009_bigger.JPG"},
        {"nombre":"Mauricio","twitter":"https://twitter.com/MaoAiz","tw-pic":"https://si0.twimg.com/profile_images/1391659719/mao_bigger.jpg"}
    ];
var integ2=[];

function fontWhite(){
    $("#members > ul li").hover(function(){
        $(this).find("div").addClass("font-white");
    },function(){
        $(this).find("div").removeClass("font-white");
    })
}

function showLateral(){
    $("#lateral").hover(function(){
        $(this).animate({
            'left':'0px'
        })
    },
    function(){
        
        $(this).animate({
            'left':'-220px'
        })
        
    }
)
}

function generarOrder(){
    integ2=generarArreglo(integ.length)
    for(i=0;i<integ.length;i++){
        $("#members ul").append("<li style='display:none'>"+
                        "<a href='"+integ[integ2[i]]["twitter"]+"' target='_blank'>"+
                            '<img class="avatar" src="'+integ[integ2[i]]["tw-pic"]+'" />'+
                            "<div>"+
                                integ[integ2[i]]["nombre"]+
                            "</div>"+
                        "</a>"+
                    "</li>")
         $("#members ul li").fadeIn(900)
    }
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
    fontWhite();
    showLateral();
}