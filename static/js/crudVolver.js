/*-----------------------------------------------------------*/
/* Función para volver desde cualquier CRUD a la página principal según categoría */
function crudVolver(){
  // Obtiene la categoría del usuario desde localStorage
  const categoria = localStorage.getItem("categoria");

  // Si es administrador, lo redirige al panel de admin
  if(categoria == "admin"){
    window.location.href = "/adminhome";
  }
  // Si es usuario normal, lo redirige al panel de home
  else if(categoria == "home"){
    window.location.href = "/home";
  }
}

/*-----------------------------------------------------------*/
/* FUNCIONES DE PRODUCTO */

/* Función para regresar al CRUD de productos según categoría */
function regresarCrudProducto() {
  let categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudproductos"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudproductos"
  }
}

/* Función para ir al formulario de agregar producto según categoría */
function irAgregarProductoFormulario() {
  let categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudproductos/agregar-producto"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudproductos/agregar-producto"
  }
}

/*-----------------------------------------------------------*/
/* FUNCIONES DE BODEGAS */

/* Función para ir a la sección de acción de producto a bodega según categoría */
function accionProductoABodega() {
  let categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudbodegas/accion-producto-a-bodega"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudbodegas/accion-producto-a-bodega"
  }
}

/* Función para ir al formulario de acción en bodegas y guardar la acción seleccionada */
function accionIrAlFormulario() {
  let categoria = localStorage.getItem("categoria")

  // Captura el valor del input donde se selecciona la acción
  let eDato = document.getElementById("accionARealizar")
  let vDato = eDato.value

  // Guarda la acción seleccionada en localStorage para usarla en el registro
  localStorage.setItem("accion", vDato);

  // Redirige al formulario correspondiente según categoría
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudbodegas/accion-producto-a-bodega/formulario-bodega"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudbodegas/accion-producto-a-bodega/formulario-bodega"
  }
}

/* Función para regresar al CRUD de bodegas según categoría */
function regresarCrudBodega() {
  let categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudbodegas"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudbodegas"
  }
}

/*-----------------------------------------------------------*/
/* FUNCIONES DE CATEGORÍAS */

/* Función para ir al formulario de agregar categoría según categoría de usuario */
function accionIrAlFormularioCategorias() {
  let categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudcategorias/formulario-categoria"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudcategorias/formulario-categoria"
  }
}

/* Función para regresar al CRUD de categorías según categoría de usuario */
function regresarCrudCategorias() {
  let categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudcategorias"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudcategorias"
  }
}
