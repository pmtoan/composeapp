const M = require('materialize-css');
const CheckUserLogin = require('./queries/CheckUserLogin');
const GetAppIdFromUrl = require('./queries/GetAppIdFromUrl');
const GetApp = require('./queries/GetApp');
const BuildApp = require('./queries/BuildApp');

window.onload = function () {
	if (CheckUserLogin()) {
		// user already login
		GetApp(GetAppIdFromUrl(), function (response) {
			document.getElementById('app_name').innerHTML = response['name'];
			document.getElementById('app_parameters').innerHTML += `
				<li class="collection-item avatar">
					<img src="/static/images/logo.png" alt="" class="circle">
					<span class="title" style="font-weight: bold">${response['desc']}</span>
					<p>
						<b>Created At: </b>${response['created_at']} <br>
						<b>Repository: </b>${response['repository']}
					</p>
					<a class="secondary-content btn-flat blue-grey-text">
						<i class="material-icons left">edit</i>
						edit
					</a>
				</li>
			`;
			for (let i=0; i<response['build_history'].length; i++) {
				let status = '';
				if (response['build_history'][i]['code'] === 0) {
					status = `
						<a class="secondary-content green-text">
							<i class="material-icons left">check</i>
							success
						</a>
					`;
				}
				else {
					status = `
						<a class="secondary-content red-text">
							<i class="material-icons left">clear</i>
							failed
						</a>
					`;
				}
				document.getElementById('build_histories').innerHTML += `
					<li class="collection-item avatar"
					onclick="window.open('/api/log/build/${response['build_history'][i]['build_id']}', '_blank');">
						<img src="/static/images/clock.png" alt="" class="circle">
						<span class="title" style="font-weight: bold">${response['build_history'][i]['built_at']}</span>
						<p>
							Build ID:  ${response['build_history'][i]['build_id']}
						</p>
						${status}
					</li>
				`;
			}
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
