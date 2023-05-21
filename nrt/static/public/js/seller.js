"use strict";

const sellerButtons = document.getElementsByClassName("generateAnswer");

function recordEvent(eventName) {
	// generate event
}

for (let i = 0; i < sellerButtons.length; i++) {
	sellerButtons[i].addEventListener(
		"click",
		() => {
			typewriterEffect(
				sellerButtons[i].getAttribute("data-id"),
				sellerButtons[i].getAttribute("data-answer")
			);
			recordEvent(sellerButtons[i].getAttribute("data-id"));
		},
		{
			once: true,
		}
	);
}
