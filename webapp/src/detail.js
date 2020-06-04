const M = require('materialize-css');
const CheckUserLogin = require('./queries/CheckUserLogin');
const GetAppIdFromUrl = require('./queries/GetAppIdFromUrl');
const GetApp = require('./queries/GetApp');
const BuildApp = require('./queries/BuildApp');

window.onload = function () {
	if (CheckUserLogin()) {
		// user already login
		GetApp(GetAppIdFromUrl(), function (response) {
			document.getElementById('app_detail').innerHTML = JSON.stringify(response);
		});

		document.getElementById('build_app').addEventListener('click', function () {
			BuildApp(GetAppIdFromUrl(), function (response) {
				if (response['code'] === 0) {
					document.getElementById('build_code').innerHTML = '<p class="green-text" style="font-weight: bold">success</p>';
				} else {
					document.getElementById('build_code').innerHTML = '<p class="red-text" style="font-weight: bold">failed</p>';
				}
				document.getElementById('build_output').innerHTML = response['output'];
				document.getElementById('build_progress').style.display = 'none';
				document.getElementById('build_status').style.display = 'block';
			});
		});

	} else {
		// go to login page
		window.location = '/app/home';
	}

	M.Modal.init(document.getElementById('build_progress_modal'), { dismissible: false });
};
