let botao = document.querySelector("#botao");
botao.style.background = "white";
let estaQuebrado = false;
let contaCliques = 0;

//botao.addEventListener("mouseover",trocaverde);

botao.addEventListener("mouseover");
    if(!estaQuebrado){
        botao.style.background = "blue";
        botao.style.color="white";
    }
    


botao.addEventListener("mouseout",e=>{
    if(estaQuebrado == false)
    botao.style.background = "green";
});

/*function trocaverde(){
    botao.style.background = "green";
}*/

botao.addEventListener("click", e =>{
    contaCliques++;
    if(contaCliques >=10){
        botao.style.background = "red";
        botao.innerHTML = "quebrei";
        estaQuebrado = true;
    }
    

});
