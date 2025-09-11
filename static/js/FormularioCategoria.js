function registrarCategorias(){
    // Captura los inputs y sus valores
    let eNombreCategoria = document.getElementById("nombreCategoria")
    let vNombreCategoria = eNombreCategoria.value

    let eDescripcionCategoria = document.getElementById("descripcionCategoria")
    let vDescripcionCategoria = eDescripcionCategoria.value

    // Captura los elementos donde se mostrarán los errores
    let eErrorNombreCategoria = document.getElementById("eNombreCategoriaE")
    let eErrorDescripcion = document.getElementById("eDescripcionCategoriaE")
    
    // Validaciones
    let vlmNombreCat = validarNull(eNombreCategoria, vNombreCategoria, eErrorNombreCategoria)
    let vlmDescripcion = validarNull(eDescripcionCategoria, vDescripcionCategoria, eErrorDescripcion)

    // Si ambos campos son válidos
    if(vlmNombreCat && vlmDescripcion){
        // Recupera el array de categorías o crea uno vacío
        let categorias = JSON.parse(localStorage.getItem("categorias")) || [];

        // Crea un objeto con los datos de la categoría
        let nuevoCategoria = {
            nombreCategria: vNombreCategoria,
            descripcion: vDescripcionCategoria
        };

        // Agrega la nueva categoría al array
        categorias.push(nuevoCategoria);

        // Guarda el array actualizado en localStorage
        localStorage.setItem("categorias", JSON.stringify(categorias));

        // Muestra el resultado en consola
        console.log(categorias)
        return true
    }
}
