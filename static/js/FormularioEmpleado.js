/*------------------------------------------------------------
FUNCION registrarEmpleados()
Se encarga de registrar un nuevo empleado en localStorage,
validando que todos los campos estén completos.
------------------------------------------------------------*/
function registrarEmpleados(){
    /*--------------------------- Captura de elementos y valores ---------------------------*/

    // Input y valor del RUT del empleado
    let eRutEmpleado = document.getElementById("rutEmpleado")
    let vRutEmpleado = eRutEmpleado.value

    // Input y valor del nombre del empleado
    let eNombreEmpleado = document.getElementById("nombreEmpleado")
    let vNombreEmpleado = eNombreEmpleado.value

    // Input y valor del apellido del empleado
    let eApellidoEmpleado = document.getElementById("apellidoEmpleado")
    let vApellidoEmpleado = eApellidoEmpleado.value

    // Input y valor de la edad del empleado
    let eEdadEmpleado = document.getElementById("edadEmpleado")
    let vEdadEmpleado = eEdadEmpleado.value

    // Input y valor del número de contacto del empleado
    let eNumeroEmpleado = document.getElementById("numeroEmpleado")
    let vNumeroEmpleado = eNumeroEmpleado.value

    /*--------------------------- Manejo de errores ---------------------------*/

    let eErrorRut = document.getElementById("eRutE")
    let eErrorNombre = document.getElementById("eNombreE")
    let eErrorApellido = document.getElementById("eApellidoE")
    let eErrorEdad = document.getElementById("eEdadE")
    let eErrorNumero = document.getElementById("eNumeroE")

    /*--------------------------- Validaciones ---------------------------*/

    // Verifica que el RUT no esté vacío
    let vlmRut = validarNull(eRutEmpleado, vRutEmpleado, eErrorRut)
    // Verifica que el nombre no esté vacío
    let vlmNombre = validarNull(eNombreEmpleado, vNombreEmpleado, eErrorNombre)
    // Verifica que el apellido no esté vacío
    let vlmApellido = validarNull(eApellidoEmpleado, vApellidoEmpleado, eErrorApellido)
    // Verifica que la edad no esté vacía
    let vlmEdad = validarNull(eEdadEmpleado, vEdadEmpleado, eErrorEdad)
    // Verifica que el número de contacto no esté vacío
    let vlmNumero = validarNull(eNumeroEmpleado, vNumeroEmpleado, eErrorNumero)

    /*--------------------------- Registro de empleado ---------------------------*/

    // Solo si todas las validaciones son correctas (true) se guarda el empleado
    if(vlmRut && vlmNombre && vlmApellido && vlmEdad && vlmNumero){
        // Recupera la lista de empleados desde localStorage o crea un array vacío si no existe
        let empleados = JSON.parse(localStorage.getItem("empleadosA")) || [];

        // Crea un objeto con todos los datos del empleado
        let nuevoEmpleado = {
            rut: vRutEmpleado,
            nombre: vNombreEmpleado,
            apellido: vApellidoEmpleado,
            edad: vEdadEmpleado,
            numero: vNumeroEmpleado
        };

        // Agrega el nuevo empleado al array
        empleados.push(nuevoEmpleado);

        // Guarda nuevamente el array actualizado en localStorage
        localStorage.setItem("empleadosA", JSON.stringify(empleados));

        // Muestra los empleados en consola (para depuración)
        console.log(empleados)

        // Retorna true indicando que el registro fue exitoso
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
        elemento.style.backgroundColor = "red"; // Fondo rojo
        elemento.style.color = "white"; // Texto blanco
        return false; // Retorna false = no válido
    } else { // Caso: el campo tiene un valor válido
        error.innerText = ""; // Limpia mensaje de error
        elemento.style.backgroundColor = "green"; // Fondo verde
        elemento.style.color = "white"; // Texto blanco
        return true; // Retorna true = válido
    }
}
