module.exports = function (id, callback) {
	const request = new XMLHttpRequest();
	request.open('POST', '/api/app/' + id, true);
	request.setRequestHeader('API_TOKEN', localStorage.getItem('_token'));
	request.onreadystatechange = function () {
		if (request.readyState === 4 && request.status === 200) {
			const response = JSON.parse(request.responseText);
			callback(response);
		}
	};
	request.send(null);
};