
function calculateCombinations() {
    const numbersInput = document.getElementById('numbers');
    const combinationsTable = document.getElementById('combinationsTable');

    const numbers = numbersInput.value;

    // Enviar los números al backend para calcular las combinaciones probables
    fetch('/calculate_combinations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ numbers }),
    })
    .then(response => response.json())
    .then(data => {
        // Limpiar la tabla antes de agregar nuevas filas
        combinationsTable.innerHTML = '';

        // Verificar si hay combinaciones para mostrar
        if (data.combinations.length > 0) {
            // Crear la primera fila con el encabezado
            const headerRow = combinationsTable.insertRow(0);
            const headerCell = headerRow.insertCell(0);
            headerCell.textContent = 'Combinaciones Probables';

            // Agregar filas con las combinaciones
            data.combinations.forEach((combination, index) => {
                const newRow = combinationsTable.insertRow(index + 1);
                const newCell = newRow.insertCell(0);
                newCell.textContent = combination;
            });
        } else {
            // Mostrar un mensaje si no hay combinaciones para mostrar
            const newRow = combinationsTable.insertRow(0);
            const newCell = newRow.insertCell(0);
            newCell.textContent = 'No hay combinaciones para mostrar.';
        }
    })
    .catch(error => console.error('Error:', error));
}
