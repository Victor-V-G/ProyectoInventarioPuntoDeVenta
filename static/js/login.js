
/*FUNCION PRINCIPAL*/
function login(){

    /*AQUI SE RECUPERA LA ID DEL INPUT DEL NOMBRE DE USUARIO Y SE ALMACENA EN LA VARIABLE ElementoNombreDeUsuario*/
    let ElementoNombreDeUsuario = document.getElementById("NombreDeUsuario")

    /*AQUI SE RECUPERA EL VALOR DEL INPUT DEL NOMBRE DE USUARIO (LO QUE INGRESO EL USUARIO) Y SE ALMACENA EN LA 
    VARIABLE ValorNombreDeUsuario*/
    let ValorNombreDeUsuario = ElementoNombreDeUsuario.value

    let eErrorNombreUsuario = document.getElementById("eErrorNombreUsuario")

    /*AQUI SE RECUPERA LA ID DEL INPUT DE LA PASSWORD Y SE ALMACENA EN LA VARIABLE ElementoPassword*/
    let ElementoPassword = document.getElementById("Password")
    
    /*AQUI SE RECUPERA EL VALOR DEL INPUT DE LA PASSWORD (LO QUE INGRESO EL USUARIO) Y SE ALMACENA EN LA 
    VARIABLE ValorPassword*/
    let ValorPassword = ElementoPassword.value

    
    let eErrorPassword = document.getElementById("eErrorPassword")

    /*AQUI SE ALMACENA EL RESULTADO DE LA FUNCION LLAMADA, EN ESTE CASO ValidarNombreDeUsuario */
    let validarNombreDeUsuario = verificarNombreDeUsuario(ElementoNombreDeUsuario, ValorNombreDeUsuario, eErrorNombreUsuario)
    
    let validarPassword = verificarPasswordUsuario(ElementoPassword, ValorPassword, eErrorPassword)

    if (validarNombreDeUsuario == 1 && validarPassword == 1){
        alert("YOU RECIVED CP")
        ElementoNombreDeUsuario.value = ""
        ElementoPassword.value = ""
        ElementoNombreDeUsuario.style.backgroundColor = "white"
        ElementoNombreDeUsuario.style.color = "black"
        ElementoPassword.style.backgroundColor = "white"
        ElementoPassword.style.color = "black"
        console.log("DALE TU CORTE PABLO  ☝ ☝ ☝ ☝ ☝ ☝")
        eErrorPassword.innerText = ""
        eErrorNombreUsuario.innerText = ""

    }
    else if (validarNombreDeUsuario == 1 && validarPassword == 1){
        alert("YOU NOT RECIVED CP")
        ElementoNombreDeUsuario.value = ""
        ElementoPassword.value = "" 
        ElementoNombreDeUsuario.style.backgroundColor = "white"
        ElementoNombreDeUsuario.style.color = "black"
        ElementoPassword.style.backgroundColor = "white"
        ElementoPassword.style.color = "black"
        eErrorPassword.innerText = ""
        eErrorNombreUsuario.innerText = ""
    }
}


function verificarNombreDeUsuario(elementoNombreUsuario,valorNombreUsuario, eErrorNombreUsuario){
    if (valorNombreUsuario.length == 0){
        elementoNombreUsuario.style.color = "white"
        elementoNombreUsuario.style.backgroundColor = "red"
        eErrorNombreUsuario.innerText = "Debes ingresar algo"
        return 0
    }
    else if (valorNombreUsuario == "admin"){
        elementoNombreUsuario.style.color = "black"
        elementoNombreUsuario.style.backgroundColor = "white"
        eErrorNombreUsuario.innerText = "Error en el nombre o contraseña"
        return 1
    }
    else if (valorNombreUsuario != "admin"){
        elementoNombreUsuario.style.color = "black"
        elementoNombreUsuario.style.backgroundColor = "white"
        eErrorNombreUsuario.innerText = "Error en el nombre o contraseña"
        return 2
    }
}


function verificarPasswordUsuario(elementoPassword, valorPassword, eErrorPassword){
    if (valorPassword.length == 0){
        elementoPassword.style.color = "white"
        elementoPassword.style.backgroundColor = "red"
        eErrorPassword.innerText = "Debes ingresar algo"
        return 0
    }
    else if (valorPassword == "123"){
        elementoPassword.style.color = "black"
        elementoPassword.style.backgroundColor = "white"
        eErrorPassword.innerText = "Error en el nombre o contraseña"
        return 1
    }
    else if (valorPassword != "123"){
        elementoPassword.style.color = "black"
        elementoPassword.style.backgroundColor = "white"
        eErrorPassword.innerText = "Error en el nombre o contraseña"
        return 2
    }
}
