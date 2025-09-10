function crudVolver(){
  const categoria = localStorage.getItem("categoria");
  if(categoria == "admin"){
    window.location.href = "/adminhome";
  }
  else if(categoria == "home"){
    window.location.href = "/home";
  }
}


function irAccionARealizarProducto() {
  let categoria = localStorage.getItem("categoria")
  
  if (categoria == "admin") {
    window.location.href = "/adminhome/crudproductos/accion-a-realizar-producto"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudproductos/accion-a-realizar-producto"
  }
}


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
    window.location.href = "/adminhome/crudproductos/accion-a-realizar-producto/agregar-producto"
  }
  else if (categoria == "home") {
    window.location.href = "/home/crudproductos/accion-a-realizar-producto/agregar-producto"
  }
}


