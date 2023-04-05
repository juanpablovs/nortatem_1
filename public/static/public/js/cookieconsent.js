"use strict";

window.addEventListener("load", function () {

    const cookieValue = document.cookie.search('nortatem_cookie_status');

    if (cookieValue === -1) {
        console.log('ahora sale');
    }
			// document.cookie = 'nortatem_cookie_status=true;';

    const cookieConsentModal = new bootstrap.Modal('#cookieconsentmodal', {
        backdrop: 'static', focus: true, keyboard: false,
    });

    cookieConsentModal.toggle()
});


// const myModal = new bootstrap.Modal(
// 	document.getElementById('myModal'), {show: true}
// );