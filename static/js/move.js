var w = screen.width;
var h = screen.height;


// mouse event
var isMousedDown = false;
var tmpX;
var tmpY;

window.addEventListener('mousedown', e => {
    isMousedDown = true;
    tmpX = e.pageX;
    tmpY = e.pageY;
});

window.addEventListener('mouseup', () => {
    isMousedDown = false;
});


// plot
var elements = document.getElementsByClassName('title');
var scale = 1.
function plot(scale) {
    elements = [].slice.call(elements);
    for (var i in elements) {
        elements[i].style.left = positions[i][0]*scale + 100*offsetX/w - 50*scale + 50 + '%';
        elements[i].style.top = positions[i][1]*scale + 100*offsetY/h - 50*scale + 50 + '%';
        elements[i].style.backgroundColor = "rgba(" + colors[i] + ", 0.5)";
    };
};


// drag event
var offsetX = 0.;
var offsetY = 0.;

function offsetUpdate() {
    offsetX = Math.sign(offsetX) * Math.min(Math.abs(offsetX), scale*w/2);
    offsetY = Math.sign(offsetY) * Math.min(Math.abs(offsetY), scale*h/2);
};

window.addEventListener('mousemove', e => {
    if (isMousedDown) {
        offsetX += e.pageX - tmpX;
        offsetY += e.pageY - tmpY;
        offsetUpdate();
        tmpX = e.pageX;
        tmpY = e.pageY;
        plot(scale);
    }
});


// wheel event
window.onmousewheel = function(event) {
    if (event.deltaY > 0) {
        scale = Math.min(4, scale + 0.03);
    } else {
        scale = Math.max(0.3, scale - 0.03);
    }
    offsetUpdate();
    plot(scale);
};


plot(scale);