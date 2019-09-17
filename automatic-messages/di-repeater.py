# -*- coding: UTF-8 -*-

from getpass import getpass
from fbchat import Client
from fbchat.models import *

# General data

THREAD_TYPE = ThreadType.GROUP
THREAD_ID = "2528752733831459"

KEYWORD_MESSAGE = "di"

# Defining the listen bot

class ListenBot(Client):

    # Overwrite the 'onMessage' method

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):

        # We check if we are in the correct conversation

        if thread_type == THREAD_TYPE and thread_id == THREAD_ID:

            # We check the receive message

            message = message_object.text

            if message.startswith(KEYWORD_MESSAGE):
                new_message = message[len(KEYWORD_MESSAGE):len(message)]

                # We send the new message

                self.send(
                    Message(text=new_message),
                    thread_id=THREAD_ID,
                    thread_type=THREAD_TYPE
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
