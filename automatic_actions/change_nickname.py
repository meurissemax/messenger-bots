###########
# Imports #
###########

from fbchat import Client
from fbchat.models import *


########
# Data #
########

KEYWORD_MESSAGE = '@nickname'


#######
# Bot #
#######

class MessengerBot(Client):

    # Constructor

    def __init__(self, username, password, thread_type, thread_id):
        self.THREAD_TYPE = thread_type
        self.THREAD_ID = thread_id

        Client.__init__(self, username, password, 'None', 1)

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
                nickname = message[len(KEYWORD_MESSAGE) + 1:len(message)]

                # We change the nickname

                try:
                    self.changeNickname(nickname, author_id, thread_id=thread_id, thread_type=thread_type)
                except FBchatException:
                    print('Request failed')
        else:
            super(MessengerBot, self).onMessage(author_id=author_id, message_object=message_object, thread_id=thread_id, thread_type=thread_type, **kwargs)
