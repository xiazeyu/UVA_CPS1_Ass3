async function fetchTemperature(room) {
    const response = await fetch(`/temperature/${encodeURIComponent(room)}`);
    const data = await response.json();
    return data;
}

function showTemperature(room) {
    fetchTemperature(room).then(temperature => {
        const temp = temperature[room];
        const display = document.getElementById("temperature-display");
        if (temp !== undefined) {
            display.innerText = `Temperature in ${room}: ${temp}°C`;
        } else {
            display.innerText = `Temperature data for ${room} is not available.`;
        }
    });
}
