path = (
	'/app/(.*)', 'Webapp',
	'/api/app/(.*)', 'ApplicationEndpoint',
	'/api/log/build/(.*)', 'BuildLogEndpoint',
	'/api/user/(.*)', 'UserEndpoint',
	'/(.*)', 'GlobalEndpoint'
)
