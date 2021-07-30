###########
# Imports #
###########

from fbchat import Client
from fbchat.models import *


########
# Data #
########

LOGOUT_MSG = 'logout' # Message to log out


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
		# Send Facebook message

		message = str(input('Message: '))

		while message != LOGOUT_MSG:
			try:
				self.send(Message(text=message), thread_id=self.THREAD_ID, thread_type=self.THREAD_TYPE)

				print('Facebook message sent.')
			except FBchatException:
				print('Request failed.')

			message = str(input('Message: '))

		# Disconnect from Facebook

		self.logout()

		print('Disconnected.')
