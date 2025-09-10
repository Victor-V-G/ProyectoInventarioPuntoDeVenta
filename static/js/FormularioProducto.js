function registrarProductos(){
    let eDatosCatProd = document.getElementById("datosCatProd")
    let vDatosCatProd = eDatosCatProd.value
    let eCodigoBarras = document.getElementById("codigoBarras")
    let vCodigoBarras = eCodigoBarras.value
    let eValorProducto = document.getElementById("valorProducto")
    let vValorProducto = eValorProducto.value
    let eStockProducto = document.getElementById("stockProducto")
    let vStockProducto = eStockProducto.value
    let eNombreProducto = document.getElementById("nombreProducto")
    let vNombreProducto = eNombreProducto.value

    let fecha = new Date();
    let fechaLocal = fecha.toLocaleDateString();

    let eMarcaProducto = document.getElementById("marcaProducto")
    let vMarcaProducto = eMarcaProducto.value
    let eFechaVencimientoProducto = document.getElementById("fechaVencimientoProducto")
    let vFechaVencimientoProducto = eFechaVencimientoProducto.value


    let productos = JSON.parse(localStorage.getItem("productos")) || [];
    let nuevoProducto = {
        categoriaProducto:vDatosCatProd,
        codigoBarras:vCodigoBarras,
        valorProducto:vValorProducto,
        stockProducto:vStockProducto,
        nombreProducto:vNombreProducto,
        fechaRegistro:fechaLocal,
        marcaProducto:vMarcaProducto,
        fechaVencimiento:vFechaVencimientoProducto
    };
    productos.push(nuevoProducto);
    localStorage.setItem("productos", JSON.stringify(productos));

    
    console.log(productos)
}