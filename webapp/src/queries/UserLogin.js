module.exports = function (username, password, callback) {
	const loginRequest = new XMLHttpRequest();
	loginRequest.open('POST', '/api/user/login', true);
	loginRequest.onreadystatechange = function () {
		if (loginRequest.readyState === 4 && loginRequest.status === 200) {
			const response = JSON.parse(loginRequest.responseText);
			if (response['code']) {
				callback(null, response['data']['token']);
			} else {
				callback(response['error'], null);
			}
		}
	};
	loginRequest.send(JSON.stringify({'username': username, 'password': password}));
};