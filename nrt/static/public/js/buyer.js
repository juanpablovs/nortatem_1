"use strict";

const buyerButtons = document.getElementsByClassName("generateAnswer");

function recordEvent(eventName) {
	// generate event
}

for (let i = 0; i < buyerButtons.length; i++) {
	buyerButtons[i].addEventListener(
		"click",
		() => {
			typewriterEffect(
				buyerButtons[i].getAttribute("data-id"),
				buyerButtons[i].getAttribute("data-answer")
			);
			recordEvent(buyerButtons[i].getAttribute("data-id"));
		},
		{
			once: true,
		}
	);
}
