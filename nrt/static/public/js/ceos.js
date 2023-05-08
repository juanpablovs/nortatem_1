"use strict";

const ceoButtons = document.getElementsByClassName("generateAnswer");

function recordEvent(eventName) {
    // generate event
}

for (let i = 0; i < ceoButtons.length; i++) {
    ceoButtons[i].addEventListener('click', () => {
		typewriterEffect(
			ceoButtons[i].getAttribute("data-id"),
			ceoButtons[i].getAttribute("data-answer")
		);
		recordEvent(ceoButtons[i].getAttribute("data-id"));
	});
}