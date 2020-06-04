const querystring = require('querystring');

module.exports = function () {
	const params = querystring.parse(window.location.toLocaleString().split('?')[1]);
	return params['app_id'];
};