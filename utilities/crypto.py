import os
import jwt
import hashlib


class InvalidToken(Exception):
	def __init__(self):
		super(self).__init__('invalid token')


class Crypto:
	@staticmethod
	def hash_password(text):
		return hashlib.sha256((os.environ['SECRET'] + text).encode()).hexdigest()

	@staticmethod
	def encode_jwt_token(data):
		try:
			token = jwt.encode(data, os.environ['SECRET'], algorithm='HS256').decode()
			return token
		except Exception as e:
			print(e)
			return None

	@staticmethod
	def decode_jwt_token(token):
		try:
			data = jwt.decode(token.encode(), os.environ['SECRET'], algorithms=['HS256'])
			return data
		except Exception as e:
			print(e)
			return InvalidToken
