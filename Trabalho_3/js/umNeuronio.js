function escolhe1neuronio(x){
    const alfa = 1;
    const limiar = 0;
    let result="a"
    let ciclos = 0
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
    let saidaDesejada = new Array(1,-1);
    var peso = new Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    var pesoNovo = new Array(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);
    var trocou = 1;
    var yin = 0;
    var b = 0;
    var bNovo = 0;
    var yliq = 0;

    while(trocou==1){
        trocou = 0;
        ciclos = ciclos+1;

        for(var j = 0 ; j<2 ; j++){
            for(var i = 0 ; i < 25 ; i++){
                yin=yin+(peso[i]*s[j][i]);
            }
            yin=yin+b;

            if(yin >= limiar){
                saida=1;
            } else {
                saida=-1;
            }

            if(saida != saidaDesejada[j]){
                trocou = 1;

                for(var i = 0 ; i < 25 ; i++){
                    pesoNovo[i] = peso[i]+(alfa*saidaDesejada[j]*s[j][i]);
                    peso[i] = pesoNovo[i];
                }
                bNovo = b+(alfa*saidaDesejada[j]);
                b = bNovo
            }
        }
    }

    for(var i = 0 ; i < 25 ; i++){
        yliq = yliq + (peso[i]*x[i])
    }
    yliq = yliq + b;
    if(yliq >= limiar){
        result = "X"
    } else{
        result = "T"
    }

    return [result, peso, b, ciclos];
    
}

document.addEventListener("DOMContentLoaded", function() {
    const treinarBtn = document.getElementById("treinarBtn");
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const visorInput = document.getElementById("visor1");
    
    treinarBtn.addEventListener("click", function() {
        const valoresArray = [];
        
        checkboxes.forEach(checkbox => {
            if (checkbox.checked) {
                valoresArray.push(1);
            } else {
                valoresArray.push(-1);
            }
        });

        
        const resultado = escolhe1neuronio(valoresArray);

        document.getElementById("visor2").value = resultado[0];
        document.getElementById("visor3").value = resultado[1];
        document.getElementById("visor4").value = resultado[2];
        document.getElementById("visor5").value = resultado[3];
    });
});