###########
# Imports #
###########

from fbchat import Client
from fbchat.models import *

import requests
import json

from datetime import datetime


########
# Data #
########

KEYWORD_MESSAGE = '@steam'

KEY_API = 'CHANGE_ME'
API_URL = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=' + KEY_API + '&steamids='


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
                steam_id = message[len(KEYWORD_MESSAGE) + 1:len(message)]

                COMPLETE_API_URL = API_URL + steam_id
                r = requests.get(COMPLETE_API_URL)
                content = json.loads(r.content)

                personaname = content['response']['players'][0]['personaname']
                lastlogoff = content['response']['players'][0]['lastlogoff']
                profileurl = content['response']['players'][0]['profileurl']

                lastlogoff_convert = datetime.utcfromtimestamp(lastlogoff).strftime('%d/%m/%Y %H:%M')

                new_message = '[BOT] Steam nickname is ' + str(personaname) + '. Last connection: ' + str(lastlogoff_convert) + '. Profile URL: ' + str(profileurl)

                # We send the message

                try:
                    self.send(Message(text=new_message), thread_id=thread_id, thread_type=thread_type)
                except FBchatException:
                    print('Request failed')
        else:
            super(MessengerBot, self).onMessage(author_id=author_id, message_object=message_object, thread_id=thread_id, thread_type=thread_type, **kwargs)
