# -*- coding: UTF-8 -*-

#######################
# Importing libraries #
#######################

from fbchat import Client
from fbchat.models import *

################
# General data #
################

KEYWORD_MESSAGE = "di"

##############################
# Defining the Messenger bot #
##############################

class MessengerBot(Client):

    # Defining constructor

    def __init__(self, username, password, thread_type, thread_id):
        self.THREAD_TYPE = thread_type
        self.THREAD_ID = thread_id

        Client.__init__(self, username, password)

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
                new_message = message[len(KEYWORD_MESSAGE):len(message)]

                # We send the new message

                try:
                    self.send(Message(text=new_message), thread_id=thread_id, thread_type=thread_type)
                except FBchatException:
                    print("Request failed (is the ID ou thread type correct ?)")
        else:
            super(MessengerBot, self).onMessage(author_id=author_id, message_object=message_object, thread_id=thread_id, thread_type=thread_type, **kwargs)