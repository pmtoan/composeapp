path = (
	'/api/app/(.*)', 'ApplicationEndpoint',
	'/api/log/build/(.*)', 'BuildLogEndpoint',
	'/(.*)', 'Root'
)
