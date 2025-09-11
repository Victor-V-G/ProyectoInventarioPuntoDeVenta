function crudVolver(){
  const categoria = localStorage.getItem("categoria");
  if(categoria == "admin"){
    window.location.href = "/adminhome";
  }
  else if(categoria == "home"){
    window.location.href = "/home";
  }
}


/*PRODUCTO FUNCION*/

function regresarCrudProducto() {
  let categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudproductos"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudproductos"
  }
}

function irAgregarProductoFormulario() {
  let categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudproductos/agregar-producto"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudproductos/agregar-producto"
  }
}


/*-------------------------------------------------------------------------------------------------*/


function accionProductoABodega() {
  let categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudbodegas/accion-producto-a-bodega"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudbodegas/accion-producto-a-bodega"
  }
}



function accionIrAlFormulario() {
  let categoria = localStorage.getItem("categoria")

  let eDato = document.getElementById("accionARealizar")
  let vDato = eDato.value
  localStorage.setItem("accion", vDato);
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudbodegas/accion-producto-a-bodega/formulario-bodega"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudbodegas/accion-producto-a-bodega/formulario-bodega"
  }
}


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


function accionIrAlFormularioCategorias() {
  let categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudcategorias/formulario-categoria"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudcategorias/formulario-categoria"
  }
}

function regresarCrudCategorias() {
  let categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudcategorias"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudcategorias"
  }
}