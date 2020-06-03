const M = require('materialize-css');
const CheckUserLogin = require('./queries/CheckUserLogin');

window.onload = function () {
	if (CheckUserLogin()) {
		// user already login
		document.getElementById('login_section').style.display = 'none';
		document.getElementById('home_section').style.display = 'block';


	} else {
		// user not login
		document.getElementById('confirm_login').addEventListener('click', function () {
			const username = document.getElementById('username').value;
			const password = document.getElementById('password').value;
			if ((username.localeCompare('') !== 0) && (password.localeCompare('') !== 0)) {
				const loginRequest = new XMLHttpRequest();
				loginRequest.open('POST', '/api/user/login', true);
				loginRequest.onreadystatechange = function () {
					if (loginRequest.readyState === 4 && loginRequest.status === 200) {
						const response = JSON.parse(loginRequest.responseText);
						if (response['token'].localeCompare('') !== 0) {
							localStorage.setItem('_token', response['token']);
							location.reload();
						} else {
							document.getElementById('login_status').innerHTML = response['error'];
						}
					}
				};
				loginRequest.send(JSON.stringify({'username': username, 'password': password}));
			}
		});
	}
	M.AutoInit();
};