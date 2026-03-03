function startTime() {
    const today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();

    // Add a leading zero to numbers less than 10
    m = checkTime(m);
    s = checkTime(s);

    // Display the time in the 'clock' div
    document.getElementById('clock').innerHTML = h + ":" + m + ":" + s;

    // Update the clock every 1000 milliseconds (1 second)
    setTimeout(startTime, 1000);
}

function checkTime(i) {
    if (i < 10) {
        i = "0" + i; // add zero in front of numbers < 10
    }
    return i;
}


window.onload = startTime();