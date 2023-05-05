"use strict";

window.addEventListener("load", function () {
    function myFunction() {
        var x = document.getElementById("myTopnav");
        if (x.className === "topnav") {
            x.className += " responsive";
        } else {
            x.className = "topnav";
        }
    }

    const navbarToggler = document.getElementById("navbar-menu-toggler");
    navbarToggler.addEventListener("click", () => {

        document.getElementById("navbar-items").classList.toggle("expand");
        navbarToggler.classList.toggle("change");
	});
});