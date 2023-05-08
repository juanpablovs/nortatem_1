"use strict";

const ceoButtons = document.getElementsByClassName("generateAnswer");

function recordEvent(eventName) {
    // generate event
}

function printAnswer(id, answer) {
    typewriterEffect(id, answer);
}


for (let i = 0; i < ceoButtons.length; i++) {
    ceoButtons[i].addEventListener('click', () => {
		recordEvent(ceoButtons[i].getAttribute("data-id"));
		printAnswer(
			ceoButtons[i].getAttribute("data-id"),
			ceoButtons[i].getAttribute("data-answer"),
		);
	});
}