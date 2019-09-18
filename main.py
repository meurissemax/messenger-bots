# -*- coding: UTF-8 -*-

#######################
# Importing libraries #
#######################

from fbchat import FBchatException
from fbchat.models import ThreadType
from getpass import getpass

##########################
# Data to change by user #
##########################

# Import the desired bot here !

from api_interactions import get_temperature as bot # do not change the 'as bot' !

# Data about the conversation

THREAD_TYPE = ThreadType.GROUP
THREAD_ID = "0000000000000000"

#################
# Main function #
#################

if __name__ == '__main__':

    # Connection to Facebook

    username = str(input("Email adress or username : "))
    password = getpass()

    try:
    	client = bot.MessengerBot(username, password, THREAD_TYPE, THREAD_ID)

    	print("Connected to Facebook.")

    	## Let's the bot does it's job

    	client.action()
    except FBchatException:
    	print("Login failed")
    except:
        print("Unknow error")
