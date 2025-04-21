

function CalculoPeso (saida1,saida2,saida3,saida4) {
        
    const entrada = new Array( 1 , 1 , 1 , -1 , -1 , 1 , -1 , -1);
    var peso1 = 0;
    var peso2 = 0;
    var peso1Novo = 0;
    var peso2Novo = 0;
    var b = 0;
    var bNovo = 0;
    const limiar = 0;
    var cont=0;
    var posi=0;
    var yliquido = 0
    var saidaCalculada = new Array( 0 , 0 , 0 , 0 );
    var saida = new Array( 0 , 0 , 0 , 0 );

    saida[0] = saida1;
    saida[1] = saida2;
    saida[2] = saida3;
    saida[3] = saida4;


    for (var i = 0 ; i < 4 ; i++){
        peso1Novo = peso1 + entrada[cont]*saida[i];
        cont++;
        peso2Novo = peso2 + entrada[cont]*saida[i];
        cont++;
        bNovo = b + saida[i];
        peso1 = peso1Novo;
        peso2 = peso2Novo;
        b = bNovo
    }

    for( var j=0 ; j<4 ; j++ ){
            
        yliquido = (peso1*entrada[posi])+b;
        posi++;
        yliquido = yliquido + (peso2*entrada[posi]);
        posi++;

        if(yliquido >= limiar){
            saidaCalculada[j]=1;
        } else {
            saidaCalculada[j]=-1;
        }
            
    }

    return [saida,saidaCalculada,peso1,peso2,b];
}  
    

function selecao(e){
    var sai1 = document.getElementById('Binario1').value
    var sai2 = document.getElementById('Binario2').value
    var sai3 = document.getElementById('Binario3').value
    var sai4 = document.getElementById('Binario4').value

    this.said1 = parseInt(sai1)
    this.said2 = parseInt(sai2)
    this.said3 = parseInt(sai3)
    this.said4 = parseInt(sai4)
    
    const result = CalculoPeso(this.said1,this.said2,this.said3,this.said4)
    result.forEach(e=>console.log(e))

    var i=10;
    result[0].forEach(e =>{
        document.querySelector(`#visor${i}`).value = e;
        i++;
    });
    var j = 1;
    result[1].forEach(e =>{
        document.querySelector(`#visor${j}`).value = e;
        j++;
    });

    document.querySelector(`#visor${5}`).value = result[2];

    document.querySelector(`#visor${6}`).value = result[3];

    document.querySelector(`#visor${7}`).value = result[4];

}
