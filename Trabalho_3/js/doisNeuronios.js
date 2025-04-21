function escolhe2neuronio(x){
    const alfa = 1;
    const limiar = 0;
    let result = "a";
    let result1= "a";
    let result2= "a";
    let ciclos1 = 0;
    let ciclos2 = 0;
    const s = new Array([1, -1, -1, -1, 1, 
                        -1, 1, -1, 1, -1, 
                        -1, -1, 1, -1, -1, 
                        -1, 1, -1, 1, -1, 
                         1, -1, -1, -1, 1],
                         [1, 1, 1, 1, 1, 
                         -1, -1, 1, -1, -1, 
                         -1, -1, 1, -1, -1,
                         -1, -1, 1, -1, -1, 
                         -1, -1, 1, -1, -1]);
    let saida = 0
    let saidaDesejada1 = new Array(1,-1);
    let saidaDesejada2 = new Array(-1,1);
    var peso1 = new Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    var peso2 = new Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    var pesoNovo1 = new Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    var pesoNovo2 = new Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    var trocou = 1;
    var yin1 = 0;
    var yin2 = 0;
    var b1 = 0;
    var b2 = 0;
    var bNovo1 = 0;
    var bNovo2 = 0
    var yliq1 = 0;
    var yliq2 = 0;

    while(trocou==1){
        trocou = 0;
        ciclos1 = ciclos1+1;

        for(var j = 0 ; j<2 ; j++){
            for(var i = 0 ; i < 25 ; i++){
                yin1=yin1+(peso1[i]*s[j][i]);
            }
            yin1=yin1+b1;

            if(yin1 >= limiar){
                saida=1;
            } else {
                saida=-1;
            }

            if(saida != saidaDesejada1[j]){
                trocou = 1;

                for(var i = 0 ; i < 25 ; i++){
                    pesoNovo1[i] = peso1[i]+(alfa*saidaDesejada1[j]*s[j][i]);
                    peso1[i] = pesoNovo1[i];
                }
                bNovo1 = b1+(alfa*saidaDesejada1[j]);
                b1 = bNovo1
            }
        }
    }
    
    trocou = 1;
    while(trocou==1){
        trocou = 0;
        ciclos2 = ciclos2+1;

        for(var j = 0 ; j<2 ; j++){
            for(var i = 0 ; i < 25 ; i++){
                yin2=yin2+(peso2[i]*s[j][i]);
            }
            yin2=yin2+b2;

            if(yin2 >= limiar){
                saida=1;
            } else {
                saida=-1;
            }

            if(saida != saidaDesejada2[j]){
                trocou = 1;

                for(var i = 0 ; i < 25 ; i++){
                    pesoNovo2[i] = peso2[i]+(alfa*saidaDesejada2[j]*s[j][i]);
                    peso2[i] = pesoNovo2[i];
                }
                bNovo2 = b2+(alfa*saidaDesejada2[j]);
                b2 = bNovo2;
            }
        }
    }

    for(var i = 0 ; i < 25 ; i++){
        yliq1 = yliq1 + (peso1[i]*x[i])
    }
    yliq1 = yliq1 + b1;
    if(yliq1 >= limiar){
        result1 = "X"
    } else{
        result1 = "T"
    }

    for(var i = 0 ; i < 25 ; i++){
        yliq2 = yliq2 + (peso2[i]*x[i])
    }
    yliq2 = yliq2 + b2;
    if(yliq2 >= limiar){
        result2 = "T"
    } else{
        result2 = "X"
    } 

    if(result1 == result2){
        result = result1;
    } else{
        result = "Não foi possível decifrar a letra."
    }

    return [result, peso1, peso2, b1, b2, ciclos1, ciclos2];
    
}

document.addEventListener("DOMContentLoaded", function() {
    const treinarBtn = document.getElementById("treinarBtn");
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    
    treinarBtn.addEventListener("click", function() {
        const valoresArray = [];
        
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                valoresArray.push(1);
            } else {
                valoresArray.push(-1);
            }
        });

        
        const resultado = escolhe2neuronio(valoresArray);

        document.getElementById("visor0").value = resultado[0];
        document.getElementById("visor1").value = resultado[1];
        document.getElementById("visor2").value = resultado[2];
        document.getElementById("visor3").value = resultado[3];
        document.getElementById("visor4").value = resultado[4];
        document.getElementById("visor5").value = resultado[5];
        document.getElementById("visor6").value = resultado[6];
    });
});