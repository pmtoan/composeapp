import uuid


def generate_uuid_v4():
	return str(uuid.uuid4())


def validate_uuid_v4(value):
	try:
		uuid.UUID(str(value))
		return True
	except ValueError:
		return False
