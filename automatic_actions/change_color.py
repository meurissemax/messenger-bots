# -*- coding: UTF-8 -*-

#######################
# Importing libraries #
#######################

from fbchat import Client
from fbchat.models import *

################
# General data #
################

KEYWORD_MESSAGE = "@color"

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
                color = message[len(KEYWORD_MESSAGE) + 1:len(message)]

                # We change the color

                if color == "messenger_blue":
                    thread_color = ThreadColor.MESSENGER_BLUE
                elif color == "viking":
                    thread_color = ThreadColor.VIKING
                elif color == "golden_poppy":
                    thread_color = ThreadColor.GOLDEN_POPPY
                elif color == "radical_red":
                    thread_color = ThreadColor.RADICAL_RED
                elif color == "shocking":
                    thread_color = ThreadColor.SHOCKING
                elif color == "picton_blue":
                    thread_color = ThreadColor.PICTON_BLUE
                elif color == "free_speech_green":
                    thread_color = ThreadColor.FREE_SPEECH_GREEN
                elif color == "pumpkin":
                    thread_color = ThreadColor.PUMPKIN
                elif color == "light_coral":
                    thread_color = ThreadColor.LIGHT_CORAL
                elif color == "medium_slate_blue":
                    thread_color = ThreadColor.MEDIUM_SLATE_BLUE
                elif color == "deep_sky_blue":
                    thread_color = ThreadColor.DEEP_SKY_BLUE
                elif color == "fern":
                    thread_color = ThreadColor.FERN
                elif color == "cameo":
                    thread_color = ThreadColor.CAMEO
                elif color == "brilliant_rose":
                    thread_color = ThreadColor.BRILLIANT_ROSE
                elif color == "biloba_flower":
                    thread_color = ThreadColor.BILOBA_FLOWER
                elif color == "tickle_me_pink":
                    thread_color = ThreadColor.TICKLE_ME_PINK
                elif color == "malachite":
                    thread_color = ThreadColor.MALACHITE
                elif color == "ruby":
                    thread_color = ThreadColor.RUBY
                elif color == "dark_tangerine":
                    thread_color = ThreadColor.DARK_TANGERINE
                elif color == "bright_turquoise":
                    thread_color = ThreadColor.BRIGHT_TURQUOISE
                else:
                    thread_color = ThreadColor.MESSENGER_BLUE

                try:
                    self.changeThreadColor(thread_color, thread_id=thread_id)
                except FBchatException:
                    print("Request failed (is the ID ou thread type correct ?)")
        else:
            super(MessengerBot, self).onMessage(author_id=author_id, message_object=message_object, thread_id=thread_id, thread_type=thread_type, **kwargs)
