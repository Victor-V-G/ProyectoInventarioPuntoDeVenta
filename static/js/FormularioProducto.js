/*------------------------------------------------------------
FUNCION registrarProductos()
Se encarga de registrar un nuevo producto en localStorage,
validando que todos los campos estén completos.
------------------------------------------------------------*/
function registrarProductos(){
    /*--------------------------- Captura de elementos y valores ---------------------------*/

    // Input y valor de la categoría del producto
    let eDatosCatProd = document.getElementById("datosCatProd")
    let vDatosCatProd = eDatosCatProd.value

    // Input y valor del código de barras
    let eCodigoBarras = document.getElementById("codigoBarras")
    let vCodigoBarras = eCodigoBarras.value

    // Input y valor del precio/valor del producto
    let eValorProducto = document.getElementById("valorProducto")
    let vValorProducto = eValorProducto.value

    // Input y valor del stock disponible
    let eStockProducto = document.getElementById("stockProducto")
    let vStockProducto = eStockProducto.value

    // Input y valor del nombre del producto
    let eNombreProducto = document.getElementById("nombreProducto")
    let vNombreProducto = eNombreProducto.value

    // Fecha actual (cuando se registra el producto)
    let fecha = new Date();
    let fechaLocal = fecha.toLocaleDateString();

    // Input y valor de la marca del producto
    let eMarcaProducto = document.getElementById("marcaProducto")
    let vMarcaProducto = eMarcaProducto.value

    // Input y valor de la fecha de vencimiento
    let eFechaVencimientoProducto = document.getElementById("fechaVencimientoProducto")
    let vFechaVencimientoProducto = eFechaVencimientoProducto.value

    /*--------------------------- Manejo de errores ---------------------------*/

    let eErrorDCP = document.getElementById("eDatosCatProdE")
    let eErrorCodigo = document.getElementById("eCodigoBarrasE")
    let eErrorValor = document.getElementById("eValorProductoE")
    let eErrorStock = document.getElementById("eStockProductoE")
    let eErrorNombre = document.getElementById("eNombreProductoE")
    let eErrorMarca = document.getElementById("eMarcaProductoE")
    let eErrorFechaV = document.getElementById("eFechaVencimientoProductoE")

    /*--------------------------- Validaciones ---------------------------*/

    // Verifica que cada campo no esté vacío
    let vlmDCP = validarNull(eDatosCatProd, vDatosCatProd, eErrorDCP)
    let vlmCodigo = validarNull(eCodigoBarras, vCodigoBarras, eErrorCodigo)
    let vlmValor = validarNull(eValorProducto, vValorProducto, eErrorValor)
    let vlmStock = validarNull(eStockProducto, vStockProducto, eErrorStock)
    let vlmNombre = validarNull(eNombreProducto, vNombreProducto, eErrorNombre)
    let vlmMarca = validarNull(eMarcaProducto, vMarcaProducto, eErrorMarca)
    let vlmFechaV = validarNull(eFechaVencimientoProducto, vFechaVencimientoProducto, eErrorFechaV)

    /*--------------------------- Registro de producto ---------------------------*/

    // Si todas las validaciones son correctas (true) se guarda el producto
    if(vlmDCP && vlmCodigo && vlmValor && vlmStock && vlmNombre && vlmMarca && vlmFechaV){
        // Recupera la lista de productos desde localStorage o crea un array vacío si no existe
        let productos = JSON.parse(localStorage.getItem("productos")) || [];

        // Crea un objeto con todos los datos del producto
        let nuevoProducto = {
            categoriaProducto: vDatosCatProd,
            codigoBarras: vCodigoBarras,
            valorProducto: vValorProducto,
            stockProducto: vStockProducto,
            nombreProducto: vNombreProducto,
            fechaRegistro: fechaLocal, // Fecha en que se registró el producto
            marcaProducto: vMarcaProducto,
            fechaVencimiento: vFechaVencimientoProducto
        };

        // Agrega el nuevo producto al array
        productos.push(nuevoProducto);

        // Guarda nuevamente el array actualizado en localStorage
        localStorage.setItem("productos", JSON.stringify(productos));

        // Muestra los productos en consola (para depuración)
        console.log(productos)

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
