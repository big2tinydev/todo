$(document).ready(function () {

    const clock = document.getElementById('clock')
    const hexColor = document.getElementById('hex-color')

    function hexClock() {
        const time = new Date();
        let hours = (time.getHours() % 12).toString();
        let minutes = time.getMinutes().toString();
        let seconds = time.getSeconds().toString();

        if (hours.length < 2) {
            hours = '0' + hours;

        }
        if (minutes.length < 2) {
            minutes = '0' + minutes;

        }
        if (seconds.length < 2) {
            seconds = '0' + seconds;

        }

        let clockString = hours + ':' + minutes + ':' + seconds;
        let hexColorString = '#' + hours + minutes + seconds;

        clock.textContent = clockString;
        hexColor.textContent = hexColorString;

        document.body.style.backgroundColor = hexColorString

    }

    hexClock()
    setInterval(hexClock, 1000)


});