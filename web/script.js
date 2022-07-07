// Onclick of the button
document.querySelector("#buttonocean").onclick = function () {
    // Call python's random_python function
    eel.random_python()(function (number) {
        // Update the div with a random number returned by python
        document.querySelector(".random_number").innerHTML = number;
    })
}
ButtonShark = document.querySelector('#buttonshark')
console.log(ButtonShark);
document.querySelector('#buttonshark').onclick = function () {
    // Call python's random_python function
    eel.f()(function () {

    })
}