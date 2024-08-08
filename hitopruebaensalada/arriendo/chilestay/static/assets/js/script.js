// script.js
$(document).ready(function() {
    // Otros scripts, si es necesario
});






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
