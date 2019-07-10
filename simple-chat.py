# -*- coding: UTF-8 -*-

from getpass import getpass
from fbchat import Client
from fbchat.models import *

if __name__ == '__main__':
	# General informations

	LOGOUT_MSG = "logout" # Message to log out

	# Connection to Facebook

	username = str(input("Email adress or username : "))
	password = getpass()
	client = Client(username, password)

	print("Connected to Facebook.")

	## Send Facebook message

	receiver_uid = str(input("Receiver UID : "))

	message = str(input("Message : "))

	while(message != LOGOUT_MSG):
		client.send(Message(text=message), thread_id=receiver_uid, thread_type=ThreadType.GROUP)

		print("Facebook message send.")

		message = str(input("Message : "))

	## Disconnect from Facebook

	client.logout()

	print("Disconnected from Facebook.")
