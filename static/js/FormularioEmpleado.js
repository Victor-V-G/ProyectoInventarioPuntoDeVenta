function registrarEmpleados(){
    let eRutEmpleado = document.getElementById("rutEmpleado")
    let vRutEmpleado = eRutEmpleado.value
    let eNombreEmpleado = document.getElementById("nombreEmpleado")
    let vNombreEmpleado = eNombreEmpleado.value
    let eApellidoEmpleado = document.getElementById("apellidoEmpleado")
    let vApellidoEmpleado = eApellidoEmpleado.value
    let eEdadEmpleado = document.getElementById("edadEmpleado")
    let vEdadEmpleado = eEdadEmpleado.value
    let eNumeroEmpleado = document.getElementById("numeroEmpleado")
    let vNumeroEmpleado = eNumeroEmpleado.value


    
    let eErrorRut = document.getElementById("eRutE")
    let eErrorNombre = document.getElementById("eNombreE")
    let eErrorApellido = document.getElementById("eApellidoE")
    let eErrorEdad = document.getElementById("eEdadE")
    let eErrorNumero = document.getElementById("eNumeroE")

    let vlmNombre = validarLargoAncho(eNombreEmpleado,vNombreEmpleado,eErrorNombre)
    let vlmApellido = validarLargoAncho(eApellidoEmpleado,vApellidoEmpleado,eErrorApellido)
    let vlmEdad = validarLargoAnchoEdad(eEdadEmpleado,vEdadEmpleado,eErrorEdad)
    

    if(vlmNombre && vlmApellido && vlmEdad){
        let empleados = JSON.parse(localStorage.getItem("empleadosA")) || [];
        let nuevoEmpleado = {
            rut:vRutEmpleado,
            nombre:vNombreEmpleado,
            apellido:vApellidoEmpleado,
            edad:vEdadEmpleado,
            numero:vNumeroEmpleado
        };
        empleados.push(nuevoEmpleado);
        localStorage.setItem("empleadosA", JSON.stringify(empleados));

    
        console.log(empleados)
    }


    
}


function validarLargoAncho(elemento,valor,error){
    valor = valor.trim()

    if(!/^[a-zA]+$/.test(valor)){
        error.innerText = "Debe ingresar algun valor tipo texto, sin espacios, ni caracteres especiales"
        elemento.style.backgroundColor = "blue"
        elemento.style.color = "white"
        return false
    }
    else if(valor.length <= 0){
        error.innerText = "Debe ingresar algun valor para el Nombre"
        elemento.style.backgroundColor = "red"
        elemento.style.color = "white"
        return false
    }
    else if(valor.length <= 2){
        error.innerText = "Debe ingresar mas de 3 caracteres para el Nombre"
        elemento.style.backgroundColor = "orange"
        elemento.style.color = "white"
        return false
    }
    else if(valor.length >= 3){
        error.innerText = "Ingresado correctamente"
        elemento.style.backgroundColor = "green"
        elemento.style.color = "white"
        return true
    }

}
    



function validarLargoAnchoEdad(elemento,valor,error){
    
    if(valor === ""){
        error.innerText = "Debe ingresar algun valor para La Edad"
        elemento.style.backgroundColor = "red"
        elemento.style.color = "white"
    }
    else if(valor >= 0 && valor <= 17){
        error.innerText = "Debe ingresar mas mayor a 18 años"
        elemento.style.backgroundColor = "orange"
        elemento.style.color = "white"
    }
    else if(valor >= 18 && valor <= 99){
        error.innerText = "Edad Ingresado correctamente"
        elemento.style.backgroundColor = "green"
        elemento.style.color = "white"
        return true
    }
    else if(valor >= 100){
        error.innerText = "Deberias estar muerto"
        elemento.style.backgroundColor = "darkred"
        elemento.style.color = "white"
    }
}