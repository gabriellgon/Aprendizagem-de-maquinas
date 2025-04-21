function getRandom(min, max) {
    return (Math.random() * (max - min)) + min;
}

function areArraysEqual(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return false;
    }

    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) {
            return false;
        }
    }

    return true;
}

function FunctNumero(x,num){

    const meu_target =[[ 1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                       [-1, 1,-1,-1,-1,-1,-1,-1,-1,-1],
                       [-1,-1, 1,-1,-1,-1,-1,-1,-1,-1],
                       [-1,-1,-1, 1,-1,-1,-1,-1,-1,-1],
                       [-1,-1,-1,-1, 1,-1,-1,-1,-1,-1],
                       [-1,-1,-1,-1,-1, 1,-1,-1,-1,-1],
                       [-1,-1,-1,-1,-1,-1, 1,-1,-1,-1],
                       [-1,-1,-1,-1,-1,-1,-1, 1,-1,-1],
                       [-1,-1,-1,-1,-1,-1,-1,-1, 1,-1],
                       [-1,-1,-1,-1,-1,-1,-1,-1,-1, 1]];  

    const limiar = 0;
    var trocou = 1;
    var ciclos = 0
    var yin = [...Array(10)].map(()=>0);
    var entrada = x;
    var peso = [];
    var pesoNovo = [];
    var b = [...Array(10)].map(()=>0);
    var bNovo = [...Array(10)].map(()=>0);
    var targetCalc = [...Array(10)].map(()=>0);
    var target = meu_target[num];
    var result = 0;

    for(var i = 0 ; i < 200 ; i++){
        peso.push(getRandom(0,1));
        pesoNovo.push(0);
    }

    while(trocou==1){
        trocou = 0;
        ciclos = ciclos + 1;
        for (var k = 0; k < 10; k++) {
            for (var i = 0; i < 20; i++) {
                var posicao = (i * 10) + k;
                yin[k] = yin[k] + (peso[posicao] * entrada[i]);
            }
            yin[k] = yin[k] + b[k];

            if (yin[k] >= limiar) {
                targetCalc[k] = 1;
            } else {
                targetCalc[k] = -1;
            }
        }
        
        if (!areArraysEqual(targetCalc, target)) {
            trocou = 1;
            for (var l = 0; l < 10; l++) {
                for (var i = 0; i < 20; i++) {
                    var posicaoPeso = (i * 10) + l;
                    pesoNovo[posicaoPeso] = peso[posicaoPeso] + (target[l] * entrada[i]);
                    peso[posicaoPeso] = pesoNovo[posicaoPeso];
                }
                bNovo[l] = b[l] + target[l];
                b[l] = bNovo[l];
            }
        }
    }

    for(var m = 0 ; m < yin.length ; m++){
        yin = [...Array(10)].map(()=>0);
        for(var i = 0 ; i < entrada.length ; i++){
            yin[m]=yin[m]+(peso[parseInt(i.toString()+m.toString())]*entrada[i]);
        }
        yin[m] = yin[m]+b[m];
        
        if(yin[m]>=limiar){
            targetCalc[m] = 1;
        } else{
            targetCalc[m] = -1;
        }
    }

    for(var i=0; i<10 ; i++){
        if(targetCalc[i]==1){
            result=i;
        }
    }

    console.log(peso);
    console.log(b);

    return [result, ciclos];
}

document.addEventListener("DOMContentLoaded", function() {
    const treinarBtn = document.getElementById("treinarBtn");
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    
    treinarBtn.addEventListener("click", function() {
        const valoresArray = [];
        let numero = document.getElementById("visor3").value;
        
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                valoresArray.push(1);
            } else {
                valoresArray.push(-1);
            }
        });
        
        const resultado = FunctNumero(valoresArray,numero);

        document.getElementById("visor2").value = resultado[0];
        document.getElementById("visor4").value = resultado[1];
    });
});