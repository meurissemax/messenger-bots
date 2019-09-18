# -*- coding: UTF-8 -*-

#######################
# Importing libraries #
#######################

import sys
sys.path.append('../')

import config

from fbchat import Client
from fbchat.models import *

################
# General data #
################

THREAD_TYPE = config.THREAD_TYPE
THREAD_ID = config.THREAD_ID

LOGOUT_MSG = "logout" # Message to log out

#################
# Main function #
#################

if __name__ == '__main__':
	
	# Connection to Facebook

	client = config.facebook_connect()

	print("Connected to Facebook.")

	# Send Facebook message

	message = str(input("Message : "))

	while(message != LOGOUT_MSG):
		try:
			client.send(
				Message(text=message),
				thread_id=THREAD_ID,
				thread_type=THREAD_TYPE
			)

			print("Facebook message send.")
		except FBchatException:
			print("Request failed (is the ID ou thread type correct ?)")


		message = str(input("Message : "))

	# Disconnect from Facebook

	client.logout()

	print("Disconnected from Facebook.")
