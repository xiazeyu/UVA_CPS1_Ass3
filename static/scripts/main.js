async function fetchTemperatures() {
    const response = await fetch('/temperatures');
    const data = await response.json();
    return data;
}

function showTemperature(room) {
    fetchTemperatures().then(temperatures => {
        const temp = temperatures[room];
        const display = document.getElementById("temperature-display");
        if (temp !== undefined) {
            display.innerText = `Temperature in ${room}: ${temp}°C`;
        } else {
            display.innerText = `Temperature data for ${room} is not available.`;
        }
    });
}
