const M = require('materialize-css');
const CheckUserLogin = require('./queries/CheckUserLogin');
const UserLogin = require('./queries/UserLogin');
const CreateApp = require('./queries/CreateApp');
const GetApp = require('./queries/GetApp');

const getApplications = function() {
	GetApp('_', function (apps) {
		for (let i=0; i<apps.length; i++) {
			let status = '';
			if (apps[i]['last_build'].localeCompare('') === 0)
				status = `
					<a class="secondary-content blue-grey-text">
						<i class="material-icons left">dashboard</i>
						draft
					</a>
				`;
			else
				status = `
					<a class="secondary-content green-text">
						<i class="material-icons left">check</i>
						deployed
					</a>
				`;

			document.getElementById('app_list').innerHTML += `
				<li class="collection-item avatar"
				onclick="window.location = '/app/detail?app_id=${apps[i]['id']}'">
					<img src="/static/images/logo.png" alt="" class="circle">
					<span class="title" style="font-weight: bold">${apps[i]['name']}</span>
					<p>
						${apps[i]['desc']} <br>
						Created At:  ${apps[i]['created_at']} <br>
						Last Build:  ${apps[i]['last_build']}
					</p>
					${status}
				</li>
			`;
		}
	});
};

window.onload = function () {
	if (CheckUserLogin()) {
		// user already login
		document.getElementById('login_section').style.display = 'none';
		document.getElementById('home_section').style.display = 'block';
		getApplications();

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
				UserLogin(username, password, function (err, token) {
					if (!err) {
						localStorage.setItem('_token', token);
						location.reload();
					} else {
						document.getElementById('login_status').innerHTML = err;
					}
				});
			}
		});
	}
	M.AutoInit();
};