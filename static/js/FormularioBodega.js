function registrarBodegas(){
    let eAccionBodega = localStorage.getItem("accion")
    let eNombreBodega = document.getElementById("nombreBodega")
    let vNombreBodega = eNombreBodega.value
    let eUbicacionBodega = document.getElementById("ubicacionBodega")
    let vUbicacionBodega = eUbicacionBodega.value



    let bodegas = JSON.parse(localStorage.getItem("bodegas")) || [];
    let nuevaBodega = {
        accion:eAccionBodega,
        nombreBodega:vNombreBodega,
        ubicacionBodega:vUbicacionBodega
    };
    bodegas.push(nuevaBodega);
    localStorage.setItem("bodegas", JSON.stringify(bodegas));

    
    console.log(bodegas)
}