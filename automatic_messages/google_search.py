# -*- coding: UTF-8 -*-

#######################
# Importing libraries #
#######################

from fbchat import Client
from fbchat.models import *

from googlesearch import search

################
# General data #
################

KEYWORD_MESSAGE = "@google"

SEARCH_TLD = "be"
SEARCH_LANG = "fr"

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
                query = message[len(KEYWORD_MESSAGE) + 1:len(message)]

                # We send the message

                for result in search(query, tld=SEARCH_TLD, lang=SEARCH_LANG, num=1, start=1, stop=1, pause=2):
                    try:
                        self.send(Message(text=result), thread_id=thread_id, thread_type=thread_type)
                    except FBchatException:
                        print("Request failed (is the ID ou thread type correct ?)")
        else:
            super(MessengerBot, self).onMessage(author_id=author_id, message_object=message_object, thread_id=thread_id, thread_type=thread_type, **kwargs)
