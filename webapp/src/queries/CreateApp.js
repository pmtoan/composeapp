module.exports = function (name, desc, repo_link, callback) {
	const request = new XMLHttpRequest();
	request.open('POST', '/api/app/_', true);
	request.setRequestHeader('API_TOKEN', localStorage.getItem('_token'));
	request.onreadystatechange = function () {
		if (request.readyState === 4 && request.status === 200) {
			const response = JSON.parse(request.responseText);
			callback(response);
		}
	};
	request.send(JSON.stringify({'name': name, 'desc': desc, 'repo_link': repo_link}));
};