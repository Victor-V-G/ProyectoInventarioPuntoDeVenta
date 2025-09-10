function registrarEmpleados(){
    let eRutEmpleado = document.getElementById("rutEmpleado")
    let vRutEmpleado = eRutEmpleado.value
    let eNombreEmpleado = document.getElementById("nombreEmpleado")
    let vNombreEmpleado = eNombreEmpleado.value
    let eApellidoEmpleado = document.getElementById("apellidoEmpleado")
    let vApellidoEmpleado = eApellidoEmpleado.value
    let eEdadEmpleado = document.getElementById("edadEmpleado")
    let vEdadEmpleado = eEdadEmpleado.value
    let eNumeroEmpleado = document.getElementById("numeroEmpleado")
    let vNumeroEmpleado = eNumeroEmpleado.value


    let empleados = JSON.parse(localStorage.getItem("empleadosA")) || [];
    let nuevoEmpleado = {
        rut:vRutEmpleado,
        nombre:vNombreEmpleado,
        apellido:vApellidoEmpleado,
        edad:vEdadEmpleado,
        numero:vNumeroEmpleado
    };
    empleados.push(nuevoEmpleado);
    localStorage.setItem("empleadosA", JSON.stringify(empleados));

    
    console.log(empleados)
}