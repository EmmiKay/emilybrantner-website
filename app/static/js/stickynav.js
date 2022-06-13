// function executed when scrolling
window.onscroll = function() {stickynav();};
var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

// function to add and remove sticky classes
function stickynav() {
if (window.pageYOffset >= sticky) {
 navbar.classList.add("stickynav");
 greenbox.classList.add("stickygb");
} else {
 navbar.classList.remove("stickynav");
 greenbox.classList.remove("stickygb");
}
}
