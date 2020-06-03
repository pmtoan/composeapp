const path = require('path');

module.exports = {
	entry: {
		'home': './webapp/src/home.js',
	},
	watch: false,
	output: {
		filename: '[name].dist.js',
		path: path.resolve(__dirname, 'static/javascripts/'),
	},
};