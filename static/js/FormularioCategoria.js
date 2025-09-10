function registrarCategorias(){
    let eNombreCategoria = document.getElementById("nombreCategoria")
    let vNombreCategoria = eNombreCategoria.value
    let eDescripcionCategoria = document.getElementById("descripcionCategoria")
    let vDescripcionCategoria = eDescripcionCategoria.value


    let categorias = JSON.parse(localStorage.getItem("categorias")) || [];
    let nuevoCategoria = {
        nombreCategoria:vNombreCategoria,
        descripcion:vDescripcionCategoria
    };
    categorias.push(nuevoCategoria);
    localStorage.setItem("categorias", JSON.stringify(categorias));

    
    console.log(categorias)
}