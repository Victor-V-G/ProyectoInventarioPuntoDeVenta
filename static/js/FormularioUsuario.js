/*------------------------------------------------------------
FUNCION registrarUsuarios()
Se encarga de registrar un nuevo usuario en localStorage,
validando previamente que los campos no estén vacíos.
------------------------------------------------------------*/
function registrarUsuarios(){
    // Obtiene el input del RUT del empleado
    let eRutEmpleado = document.getElementById("rutEmpleado")
    // Obtiene el valor ingresado en el input del RUT
    let vRutEmpleado = eRutEmpleado.value

    // Obtiene el input del cargo del usuario
    let eCargoUsuario = document.getElementById("cargoUsuario")
    // Obtiene el valor ingresado en el input del cargo
    let vCargoUsuario = eCargoUsuario.value

    // Obtiene el input de la contraseña
    let eContraseniaUsuario = document.getElementById("contraseniaUsuario")
    // Obtiene el valor ingresado en el input de la contraseña
    let vContraseniaUsuario = eContraseniaUsuario.value

    /*--------------------------- Manejo de errores ---------------------------*/

    // Span donde se mostrará error en caso de que falte el RUT
    let eErrorRutEmpleado = document.getElementById("eRutE")
    // Span donde se mostrará error en caso de que falte el cargo
    let eErrorCargoUsuario = document.getElementById("eCargoE")
    // Span donde se mostrará error en caso de que falte la contraseña
    let eErrorContrasenia = document.getElementById("eContraseniaUsuarioE")

    /*--------------------------- Validaciones ---------------------------*/

    // Verifica que el RUT no esté vacío
    let vlmRut = validarNull(eRutEmpleado, vRutEmpleado, eErrorRutEmpleado)
    // Verifica que el cargo no esté vacío
    let vlmCargo = validarNull(eCargoUsuario, vCargoUsuario, eErrorCargoUsuario)
    // Verifica que la contraseña no esté vacía
    let vlmpass = validarNull(eContraseniaUsuario, vContraseniaUsuario, eErrorContrasenia)

    /*--------------------------- Registro de usuario ---------------------------*/

    // Solo si las tres validaciones son correctas (true) se guarda el usuario
    if(vlmRut && vlmCargo && vlmpass){
        // Recupera los usuarios desde localStorage o crea un array vacío si no existen
        let usuarios = JSON.parse(localStorage.getItem("usuarios")) || [];

        // Crea un objeto con los datos del nuevo usuario
        let nuevoUsuario = {
            rut: vRutEmpleado,
            cargo: vCargoUsuario,
            contrasenia: vContraseniaUsuario
        };

        // Agrega el nuevo usuario al array
        usuarios.push(nuevoUsuario);

        // Guarda nuevamente el array de usuarios en localStorage
        localStorage.setItem("usuarios", JSON.stringify(usuarios));

        // Muestra en consola el listado de usuarios (para verificar)
        console.log(usuarios)

        // Retorna true para indicar que el registro fue exitoso
        return true
    }
    
}


/*------------------------------------------------------------
FUNCION validarNull()
Valida si un campo está vacío o no, y cambia el estilo del input
dependiendo del resultado.
------------------------------------------------------------*/
function validarNull(elemento, valor, error) {
    if (valor.length === 0) { // Caso: el campo está vacío
        error.innerText = "Debe ingresar un valor"; // Muestra mensaje de error
        elemento.style.backgroundColor = "red"; // Fondo rojo (error)
        elemento.style.color = "white"; // Texto blanco
        return false; // Retorna false = no válido
    } else { // Caso: el campo tiene algún valor
        error.innerText = ""; // Limpia el mensaje de error
        elemento.style.backgroundColor = "green"; // Fondo verde (válido)
        elemento.style.color = "white"; // Texto blanco
        return true; // Retorna true = válido
    }
}
