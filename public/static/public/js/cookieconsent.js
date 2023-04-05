"use strict";

window.addEventListener("load", function () {

    // document.cookie = 'nortatem_cookie_status=true;';
    const cookieValue = document.cookie.search('nortatem_cookie_status');

    console.log(cookieValue, cookieValue === -1);

    const cookieConsentModal = new bootstrap.Modal('#cookieconsentmodal', {
        keyboard: false, show: true,
    });

    cookieConsentModal.show()
});


// const myModal = new bootstrap.Modal(
// 	document.getElementById('myModal'), {show: true}
// );