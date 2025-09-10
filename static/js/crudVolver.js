function crudVolver(){
  const categoria = localStorage.getItem("categoria");
  if(categoria == "admin"){
    window.location.href = "/adminhome";
  }
  else if(categoria == "home"){
    window.location.href = "/home";
  }
}




