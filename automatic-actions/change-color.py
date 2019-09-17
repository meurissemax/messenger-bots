# -*- coding: UTF-8 -*-

from getpass import getpass
from fbchat import Client
from fbchat.models import *

# General data

THREAD_TYPE = ThreadType.GROUP
THREAD_ID = "2528752733831459"

KEYWORD_MESSAGE = "@color"

# Defining the listen bot

class ListenBot(Client):

    # Overwrite the 'onMessage' method

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):

        # We check if we are in the correct conversation

        if thread_type == THREAD_TYPE and thread_id == THREAD_ID:

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
                    thread_color = ThreadColor.MESSENGER_RED

                self.changeThreadColor(
                    thread_color,
                    thread_id=thread_id
                )
        else:
            super(ListenBot, self).onMessage(
                author_id=author_id,
                message_object=message_object,
                thread_id=thread_id,
                thread_type=thread_type,
                **kwargs
            )

if __name__ == '__main__':

    # Connection to Facebook

    username = str(input("Email adress or username : "))
    password = getpass()
    client = ListenBot(username, password)

    print("Connected to Facebook.")

    # Let's the bot does it's job

    client.listen()
