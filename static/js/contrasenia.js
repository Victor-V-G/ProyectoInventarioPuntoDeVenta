document.addEventListener("DOMContentLoaded", function () {
    const checkbox = document.getElementById("id_CambiarPassword");
    const campos = document.getElementById("password-fields");

    if (!checkbox || !campos) return; // seguridad por si no existen

    // Ocultar los campos al inicio
    campos.style.display = checkbox.checked ? "block" : "none";

    // Detectar el cambio y mostrar/ocultar dinámicamente
    checkbox.addEventListener("change", function () {
        campos.style.display = this.checked ? "block" : "none";
    });
});