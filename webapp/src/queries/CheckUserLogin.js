module.exports = function () {
	const token = localStorage.getItem('_token');
	return token !== undefined && token !== null;
};