import datetime


def current_timestamp():
	return str(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S'))
