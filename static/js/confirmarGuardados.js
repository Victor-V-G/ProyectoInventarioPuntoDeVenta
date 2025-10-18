document.addEventListener('DOMContentLoaded', function() {
    // Selecciona el botón "Guardar" en el formulario del Admin
    const BotonDeGuardado = document.querySelector('input[name="_save"]');
    const BotonDeGuardado1 = document.querySelector('input[name="_addanother"]');
    const BotonDeGuardado2 = document.querySelector('input[name="_continue"]');

    if (BotonDeGuardado) {
        BotonDeGuardado.addEventListener('click', function(e) {
            // Muestra confirmación antes de guardar
            if (!confirm('¿Seguro que deseas guardar esta edicion?')) {
                e.preventDefault();  // Cancela el guardado si el usuario presiona "Cancelar"
            }
        });
    }
    if (BotonDeGuardado1) {
        BotonDeGuardado1.addEventListener('click', function(e) {
            // Muestra confirmación antes de guardar
            if (!confirm('¿Seguro que deseas guardar y agregar otra edicion?')) {
                e.preventDefault();  // Cancela el guardado si el usuario presiona "Cancelar"
            }
        });
    }
    if (BotonDeGuardado2) {
        BotonDeGuardado2.addEventListener('click', function(e) {
            // Muestra confirmación antes de guardar
            if (!confirm('¿Seguro que deseas guardar y seguir editando esta edicion?')) {
                e.preventDefault();  // Cancela el guardado si el usuario presiona "Cancelar"
            }
        });
    }
});
