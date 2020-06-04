const M = require('materialize-css');
const CheckUserLogin = require('./queries/CheckUserLogin');
const GetAppIdFromUrl = require('./queries/GetAppIdFromUrl');
const GetApp = require('./queries/GetApp');

window.onload = function () {
	if (CheckUserLogin()) {
		// user already login
		GetApp(GetAppIdFromUrl(), function (response) {
			document.getElementById('app_detail').innerHTML = JSON.stringify(response);
		});

		document.getElementById('build_app').addEventListener('click', function () {
			setInterval(function () {
				location.reload();
			}, 5000);
		});

	} else {
		// go to login page
		window.location = '/app/home';
	}

	M.Modal.init(document.getElementById('build_progress_modal'), { dismissible: false });
};
