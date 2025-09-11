function registrarUsuarios(){
    let eRutEmpleado = document.getElementById("rutEmpleado")
    let vRutEmpleado = eRutEmpleado.value
    let eCargoUsuario = document.getElementById("cargoUsuario")
    let vCargoUsuario = eCargoUsuario.value
    let eContraseniaUsuario = document.getElementById("contraseniaUsuario")
    let vContraseniaUsuario = eContraseniaUsuario.value


    let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];
    let nuevoUsuario = {
        rut:vRutEmpleado,
        cargo:vCargoUsuario,
        contrasenia:vContraseniaUsuario
    };
    usuarios.push(nuevoUsuario);
    localStorage.setItem("usuarios", JSON.stringify(usuarios));

    
    console.log(usuarios)
}