module.exports = function (username, password, callback) {
	const loginRequest = new XMLHttpRequest();
	loginRequest.open('POST', '/api/user/login', true);
	loginRequest.onreadystatechange = function () {
		if (loginRequest.readyState === 4 && loginRequest.status === 200) {
			const response = JSON.parse(loginRequest.responseText);
			callback(response);
		}
	};
	loginRequest.send(JSON.stringify({'username': username, 'password': password}));
};