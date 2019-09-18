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

KEYWORD_MESSAGE = "@nickname"

###########################
# Defining the listen bot #
###########################

class ListenBot(Client):

    # Overwrite the 'onMessage' method

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):

        # We check if we are in the correct conversation

        if thread_type == THREAD_TYPE and thread_id == THREAD_ID:

            # We check the receive message

            message = message_object.text

            if message.startswith(KEYWORD_MESSAGE):
                nickname = message[len(KEYWORD_MESSAGE) + 1:len(message)]

                # We change the nickname

                try:
                    self.changeNickname(
                        nickname,
                        author_id,
                        thread_id=thread_id,
                        thread_type=thread_type
                    )
                except FBchatException:
                    print("Request failed (is the ID ou thread type correct ?)")
        else:
            super(ListenBot, self).onMessage(
                author_id=author_id,
                message_object=message_object,
                thread_id=thread_id,
                thread_type=thread_type,
                **kwargs
            )

#################
# Main function #
#################

if __name__ == '__main__':

    # Connection to Facebook

    client = config.facebook_connect()

    print("Connected to Facebook.")

    # Let's the bot does it's job

    client.listen()
