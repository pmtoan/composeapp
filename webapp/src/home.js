const M = require('materialize-css');
const CheckUserLogin = require('./queries/CheckUserLogin');
const UserLogin = require('./queries/UserLogin');
const CreateApp = require('./queries/CreateApp');
const GetApp = require('./queries/GetApp');

window.onload = function () {
	if (CheckUserLogin()) {
		// user already login
		document.getElementById('login_section').style.display = 'none';
		document.getElementById('home_section').style.display = 'block';

		GetApp('_', function (apps) {
			for (let i=0; i<apps.length; i++) {
				document.getElementById('app_list').innerHTML += `
					<div class="col s12" style="margin-bottom: 10px;">
						<a class="btn btn-large white blue-grey-text">
							<i class="material-icons left">dashboard</i>
							${apps[i]['name']}
						</a>
					</div>
				`;
			}
		});

		document.getElementById('confirm_create_app').addEventListener('click', function () {
			const name = document.getElementById('app_name').value;
			const desc = document.getElementById('app_desc').value;
			const repo_link = document.getElementById('app_repo').value;
			if ((name.localeCompare('') !== 0) && (repo_link.localeCompare('') !== 0)) {
				CreateApp(name, desc, repo_link, function (response) {
					if (response['error'].localeCompare('') !== 0) {
						document.getElementById('create_app_status').innerHTML = response['error'];
					} else {
						location.reload();
					}
				});
			}
		});

	} else {
		// user not login
		document.getElementById('confirm_login').addEventListener('click', function () {
			const username = document.getElementById('username').value;
			const password = document.getElementById('password').value;
			if ((username.localeCompare('') !== 0) && (password.localeCompare('') !== 0)) {
				UserLogin(username, password, function (response) {
					if (response['token'].localeCompare('') !== 0) {
						localStorage.setItem('_token', response['token']);
						location.reload();
					} else {
						document.getElementById('login_status').innerHTML = response['error'];
					}
				});
			}
		});
	}
	M.AutoInit();
};