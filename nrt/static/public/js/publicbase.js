"use strict";

const navbarToggler = document.getElementById("navbar-menu-toggler");
navbarToggler.addEventListener("click", () => {
	document.getElementById("navbar-items").classList.toggle("expand");
	navbarToggler.classList.toggle("change");
});

function typewriterEffect(elementId, text, speed = 120) {
	let i = 0;
	const textLength = text.length;

	function typeWriter() {
		if (i < textLength) {
			document.getElementById(elementId).innerHTML += text.charAt(i);
			i++;
			setTimeout(typeWriter, speed);
		}
	}

	typeWriter();
}
