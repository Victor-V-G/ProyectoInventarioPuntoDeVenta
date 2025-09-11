function registrarBodegas(){
    // Recupera el valor de "accion" almacenado previamente en localStorage
    let eAccionBodega = localStorage.getItem("accion")

    // Captura el input del nombre de la bodega y su valor
    let eNombreBodega = document.getElementById("nombreBodega")
    let vNombreBodega = eNombreBodega.value

    // Captura el input de la ubicación de la bodega y su valor
    let eUbicacionBodega = document.getElementById("ubicacionBodega")
    let vUbicacionBodega = eUbicacionBodega.value

    // Captura los elementos donde se mostrarán los errores
    let eErrorNombre = document.getElementById("eNombreBodegaE")
    let eErrorUbicacion = document.getElementById("eUbicacionBodegaE")
    
    // Valida que los campos no estén vacíos usando la función validarNull
    let vlvNombre = validarNull(eNombreBodega, vNombreBodega, eErrorNombre)
    let vlvUbicacion = validarNull(eUbicacionBodega, vUbicacionBodega, eErrorUbicacion)

    // Si ambos campos son válidos, se procede a registrar la bodega
    if(vlvNombre && vlvUbicacion){
        // Recupera el array de bodegas guardado en localStorage o crea uno vacío
        let bodegas = JSON.parse(localStorage.getItem("bodegas")) || [];

        // Crea un objeto con los datos de la nueva bodega
        let nuevaBodega = {
            accion: eAccionBodega,         // Acción tomada al registrar (puede venir de otra función)
            nombreBodega: vNombreBodega,   // Nombre de la bodega ingresado por el usuario
            ubicacionBodega: vUbicacionBodega // Ubicación ingresada por el usuario
        };

        // Agrega la nueva bodega al array
        bodegas.push(nuevaBodega);

        // Guarda el array actualizado en localStorage
        localStorage.setItem("bodegas", JSON.stringify(bodegas));

        // Muestra el array de bodegas en consola
        console.log(bodegas)
        return true
    }
}

// Función para validar que un input no esté vacío
function validarNull(elemento, valor, error) {
    if (valor.length === 0) {
        // Si está vacío, muestra el mensaje de error y cambia el fondo del input a rojo
        error.innerText = "Debe ingresar un valor";
        elemento.style.backgroundColor = "red";
        elemento.style.color = "white";
        return false;
    } else {
        // Si tiene valor, borra el mensaje de error y cambia el fondo a verde
        error.innerText = "";
        elemento.style.backgroundColor = "green";
        elemento.style.color = "white";
        return true;
    }
}
