import os
import jwt
import hashlib


def generate_password_hash(text):
	return hashlib.sha256(text.encode()).hexdigest()


def encode_jwt_token(data):
	return jwt.encode(data, os.environ['SECRET'], algorithm='HS256')


def decode_jwt_token(token):
	return jwt.decode(token, os.environ['SECRET'], algorithms=['HS256'])
