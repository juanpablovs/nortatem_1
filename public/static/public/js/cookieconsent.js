'use strict';

window.addEventListener('load', function () {
	const cookieValue = document.cookie.search('nortatem_cookie_status');

	if (cookieValue === -1) {
		const cookieConsentModal = new bootstrap.Modal('#cookieconsentmodal', {
			backdrop: 'static',
			focus: true,
			keyboard: false,
		});

		cookieConsentModal.show();

		const cookieConsentButtonAccept = document.getElementById(
			'cookieconsentbuttonaccept',
		);

		cookieConsentButtonAccept.addEventListener(
			'click',
			() => {
				document.cookie = 'nortatem_cookie_status=true;max-age=31536000';
				cookieConsentModal.hide();
			},
			{
				once: true,
			},
		);
	}
});
