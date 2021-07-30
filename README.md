# Messenger bots

This project consists of a series of bots for [Facebook Messenger](https://www.messenger.com/).

The bots were made in [Python 3](https://www.python.org/) mainly using the library [fbchat](https://fbchat.readthedocs.io/en/latest/).

## Warning

These bots were created for **recreational purposes**.

Their use **must not** in any way violate Facebook's rules. In particular, these bots **must not be used for spam or unwanted advertising**.

Here you are, adventurer! We will not be responsible for your sanctions if you have any.

## Use the bots

First, create and activate the Anaconda environment using
```
conda env create -f environment.yml
conda activate messenger-bots
```

Second, import the bot you want to use by editing the appropriate import in the `main.py` file.
```python
from THE_PACKAGE_YOU_WANT import THE_BOT_YOU_WANT as bot # do not change the 'as bot' !
# Example: from simple_interactions import simple_chat as bot
```

Finally, run the `main.py` file by using
```python
python main.py -username USERNAME -password PASSWORD -type THREAD_TYPE -id THREAD_ID
```

* The username is your Facebook username (or email address). Let it empty to manually enter it when script is running.
* The password is your Facebook password. Let it empty to manually enter it when script is running.
* The thread type defines the type of your conversation: `user` for a conversation with a single user and `group` for a group conversation.
* The thread ID is a unique identifier of your conversation and can be found in the URL of the conversation or via external tools.

## Create your own bot

To implement your own bot, use the following template and implement the `action` method. Save it as a Python file (`.py`) and import your bot in the `main.py` file.
```python
###########
# Imports #
###########

from fbchat import Client
from fbchat.models import *


#######
# Bot #
#######

class MessengerBot(Client):

    # Constructor

    def __init__(self, username, password, thread_type, thread_id):
        self.THREAD_TYPE = thread_type
        self.THREAD_ID = thread_id

        Client.__init__(self, username, password)

	# Defining the 'action' method

	def action(self):
    	    # action that the bot has to do

```
