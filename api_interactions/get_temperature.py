# -*- coding: UTF-8 -*-

#######################
# Importing libraries #
#######################

from fbchat import Client
from fbchat.models import *

import requests
import json

################
# General data #
################

KEYWORD_MESSAGE = "@temperature"
API_URL = "https://www.prevision-meteo.ch/services/json/CHANGE_ME"

##############################
# Defining the Messenger bot #
##############################

class MessengerBot(Client):

    # Defining constructor

    def __init__(self, username, password, thread_type, thread_id):
        self.THREAD_TYPE = thread_type
        self.THREAD_ID = thread_id

        Client.__init__(self, username, password, "None", 1)

    # Defining the 'action' method

    def action(self):
        self.listen()

    # Overwrite the 'onMessage' method

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):

        # We check if we are in the correct conversation

        if thread_type == self.THREAD_TYPE and thread_id == self.THREAD_ID:

            # We check the receive message

            message = message_object.text

            if message.startswith(KEYWORD_MESSAGE):
                r = requests.get(API_URL)
                content = json.loads(r.content)

                temperature = content['current_condition']['tmp']

                new_message = "[BOT] La température est actuellement de " + str(temperature) + " degrés celsius."

                # We send the message

                try:
                    self.send(Message(text=new_message), thread_id=thread_id, thread_type=thread_type)
                except FBchatException:
                    print("Request failed (is the ID ou thread type correct ?)")
        else:
            super(MessengerBot, self).onMessage(author_id=author_id, message_object=message_object, thread_id=thread_id, thread_type=thread_type, **kwargs)
