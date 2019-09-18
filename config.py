# -*- coding: UTF-8 -*-

#######################
# Importing libraries #
#######################

from fbchat import Client
from fbchat.models import *

from getpass import getpass

#########################################################
# Information about the Facebook Messenger conversation #
#########################################################

'''
Thread Type
-----------

The thread type defines the type of the conversation : a conversion
with another person or a group conversation.

For a conversation with a single user : 	ThreadType.USER
For a group conversation : 					ThreadType.GROUP
'''

THREAD_TYPE = ThreadType.GROUP

'''
Thread ID
---------

The thread ID is the unique ID of the conversation. This ID can be
found in the URL of the conversation or via external tools
'''

THREAD_ID = "change_me"

#############
# Functions #
#############

'''
facebook_connect()
------------------

This function is used to connect the bot to a Facebook account.
'''

def facebook_connect():
	username = str(input("Email adress or username : "))
	password = getpass()

	return Client(username, password)
