var display = document.getElementById('display');
display.style.position = "absolute";


var onDisplayMove = function (e) {
    var x = e.clientX;
    var y = e.clientY;
    // var width = display.offsetWidth;
    // var height = display.offsetHeight;
    display.style.top = y + "px";
    display.style.left = x + "px";
};

display.onmousedown = function(e){
    document.addEventListener("mousemove", onDisplayMove);
};

display.onmouseup = function(e) {
    document.removeEventListener("mousemove",onDisplayMove);
}