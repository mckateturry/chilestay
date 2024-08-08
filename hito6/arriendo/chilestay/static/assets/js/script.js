// static/js/script.js

function filtrarComunas(regionId) {
    console.log('Region ID selected:', regionId); // Verifica el ID de la región seleccionada
    if (!regionId) {
        document.getElementById('comuna').innerHTML = '<option value="">Todas las comunas</option>';
        return;
    }

    axios.post('/filtrar-comunas/', { regionId: regionId })
        .then(response => {
            console.log('Response data:', response.data); // Verifica la respuesta del servidor
            if (response.data.status === 200) {
                const comunas = response.data.data;
                let options = '<option value="">Todas las comunas</option>';
                comunas.forEach(comuna => {
                    options += `<option value="${comuna.id}">${comuna.name}</option>`;
                });
                document.getElementById('comuna').innerHTML = options;
            } else {
                console.error('Error:', response.data);
            }
        })
        .catch(error => {
            console.error('Error al filtrar comunas:', error);
        });
}















// function filtrarComunas(regionId) {
//     if (!regionId) {
//         document.getElementById('comunas').innerHTML = '<option value="">Seleccione</option>';
//         return;
//     }

//     axios.post('/filtrar-comunas/', { regionId: regionId })
//         .then(response => {
//             if (response.data.status === 200) {
//                 const comunas = response.data.data;
//                 let options = '<option value="">Seleccione</option>';
//                 comunas.forEach(comuna => {
//                     options += `<option value="${comuna.id}">${comuna.name}</option>`;
//                 });
//                 document.getElementById('comunas').innerHTML = options;
//             } else {
//                 console.error('Error:', response.data);
//             }
//         })
//         .catch(error => {
//             console.error('Error al filtrar comunas:', error);
//         });
// }
