const M = require('materialize-css');
const querystring = require('querystring');
const CheckUserLogin = require('./queries/CheckUserLogin');
const GetApp = require('./queries/GetApp');

window.onload = function () {
	if (CheckUserLogin()) {
		// user already login
		const params = querystring.parse(window.location.toLocaleString().split('?')[1]);
		if ((params['app_id'] !== undefined) && (params['app_id'] !== null) && (params['app_id'] !== '')) {
			GetApp(params['app_id'], function (response) {
				document.getElementById('app_detail').innerHTML = JSON.stringify(response);
			});
		}

	} else {
		// go to login page
		window.location = '/app/home';
	}
};
