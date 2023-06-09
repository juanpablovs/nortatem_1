"use strict";

const cookieValue = document.cookie.search("nortatem_cookie_status");

if (cookieValue === -1) {
	document.getElementById("cookieconsent").style.display = "block";

	const cookieConsentButtonAccept = document.getElementById(
		"cookieconsentbuttonaccept"
	);

	cookieConsentButtonAccept.addEventListener(
		"click",
		() => {
			document.cookie =
				"nortatem_cookie_status=true;max-age=31536000;path=/";
			document.getElementById("cookieconsent").style.display = "none";
		},
		{
			once: true,
		}
	);
}
