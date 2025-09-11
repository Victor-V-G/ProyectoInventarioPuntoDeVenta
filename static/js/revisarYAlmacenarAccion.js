
function registrarEmpleadosAccion() {
    let fechaRegistro = new Date();
    let fechaLocalRegistro = fechaRegistro.toLocaleDateString();
    let horaRegistro = fechaRegistro.toLocaleTimeString();

    let accion = {
        tipo: "Registrar Empleado",
        fecha: fechaLocalRegistro,
        hora: horaRegistro
    }

    if (!localStorage.getItem("Acciones")) {
        localStorage.setItem("Acciones", JSON.stringify([]));
    }

    let acciones = JSON.parse(localStorage.getItem("Acciones"))

    acciones.push(accion);

    localStorage.setItem("Acciones", JSON.stringify(acciones))
}


function registrarUsuariosAccion() {
    let fechaRegistro = new Date();
    let fechaLocalRegistro = fechaRegistro.toLocaleDateString();
    let horaRegistro = fechaRegistro.toLocaleTimeString();

    let accion = {
        tipo: "Registrar Usuarios",
        fecha: fechaLocalRegistro,
        hora: horaRegistro
    }

    if (!localStorage.getItem("Acciones")) {
        localStorage.setItem("Acciones", JSON.stringify([]));
    }

    let acciones = JSON.parse(localStorage.getItem("Acciones"))

    acciones.push(accion);

    localStorage.setItem("Acciones", JSON.stringify(acciones))
}


function registrarProductosAccion() {
    let fechaRegistro = new Date();
    let fechaLocalRegistro = fechaRegistro.toLocaleDateString();
    let horaRegistro = fechaRegistro.toLocaleTimeString();

    let accion = {
        tipo: "Registrar Productos",
        fecha: fechaLocalRegistro,
        hora: horaRegistro
    }

    if (!localStorage.getItem("Acciones")) {
        localStorage.setItem("Acciones", JSON.stringify([]));
    }

    let acciones = JSON.parse(localStorage.getItem("Acciones"))

    acciones.push(accion);

    localStorage.setItem("Acciones", JSON.stringify(acciones))
}


function registrarCategoriaAccion() {
    let fechaRegistro = new Date();
    let fechaLocalRegistro = fechaRegistro.toLocaleDateString();
    let horaRegistro = fechaRegistro.toLocaleTimeString();

    let accion = {
        tipo: "Registrar Categoria",
        fecha: fechaLocalRegistro,
        hora: horaRegistro
    }

    if (!localStorage.getItem("Acciones")) {
        localStorage.setItem("Acciones", JSON.stringify([]));
    }

    let acciones = JSON.parse(localStorage.getItem("Acciones"))

    acciones.push(accion);

    localStorage.setItem("Acciones", JSON.stringify(acciones))
}


function registrarProductoABodegaAccion() {
    let fechaRegistro = new Date();
    let fechaLocalRegistro = fechaRegistro.toLocaleDateString();
    let horaRegistro = fechaRegistro.toLocaleTimeString();

    let accion = {
        tipo: "Registrar Producto a Bodega",
        fecha: fechaLocalRegistro,
        hora: horaRegistro
    }

    if (!localStorage.getItem("Acciones")) {
        localStorage.setItem("Acciones", JSON.stringify([]));
    }

    let acciones = JSON.parse(localStorage.getItem("Acciones"))

    acciones.push(accion);

    localStorage.setItem("Acciones", JSON.stringify(acciones))
}