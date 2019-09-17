# -*- coding: UTF-8 -*-

from getpass import getpass
from fbchat import Client
from fbchat.models import *

# General data

THREAD_TYPE = ThreadType.GROUP
THREAD_ID = "2528752733831459"

LOGOUT_MSG = "logout" # Message to log out

if __name__ == '__main__':
	
	# Connection to Facebook

	username = str(input("Email adress or username : "))
	password = getpass()
	client = Client(username, password)

	print("Connected to Facebook.")

	# Send Facebook message

	message = str(input("Message : "))

	while(message != LOGOUT_MSG):
		client.send(
			Message(text=message),
			thread_id=THREAD_ID,
			thread_type=THREAD_TYPE
		)

		print("Facebook message send.")

		message = str(input("Message : "))

	# Disconnect from Facebook

	client.logout()

	print("Disconnected from Facebook.")
