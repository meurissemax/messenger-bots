# Messenger bots

This project consists of a series of bots for [Facebook Messenger](https://www.messenger.com/).

The bots were made in [Python](https://www.python.org/downloads/release/python-370/) (version 3.7) mainly using the library [fbchat](https://fbchat.readthedocs.io/en/latest/).

## Warning !

These bots were created for **recreational purposes**.

Their use **must not** in any way violate Facebook's rules. In particular, these bots **must not be used for spam or unwanted advertising**.

Here you are, adventurer ! We will not be responsible for your sanctions if you have any.

## How to use bots ?

To use the bots, you must at least install [Python](https://www.python.org/downloads/release/python-370/) (version 3.7) and the [fbchat](https://fbchat.readthedocs.io/en/latest/) library :
```
pip3 install fbchat
```

After that, you simply have to edit this section in the `main.py` file :
```python
##########################
# Data to change by user #
##########################

# Import the desired bot here !

from api_interactions import get_temperature as bot # do not change the 'as bot' !

# Data about the conversation

THREAD_TYPE = ThreadType.GROUP
THREAD_ID = "0000000000000000"
```

* The first line of code is about the *bot you want to use*. You simply have to import it. In this example, the imported bot is **get_temperature** from the package **api_interactions**. The `as bot` can't be change !
* The second line of code is about the *thread type*. The thread type defined the type of your conversation : `ThreadType.USER` for a conversation with a single user and `ThreadType.GROUP` for a group conversation.
* The third line of code is about the *thread ID*. This ID is a unique identifier of your conversation and can be found in the URL of the conversation or via external tools.
 
When the file `main.py` has been configured, all that remains is to launch a bot with the command :
```
python3 main.py
```

### Additionnal libraires

Some bots use additional Python libraries. Here is the complete list of all the additional libraries uses :

* [google](https://pypi.org/project/google/)

## Create your own bot

The basic template of a bot is :
```python
# -*- coding: UTF-8 -*-

#######################
# Importing libraries #
#######################

from fbchat import Client
from fbchat.models import *

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
    	    # action that the bot has to do

```

You simply have to set the `action` method with the action that your bot has to do. Save this as a python file and import it in the `main.py` file.

## Author

* **Maxime Meurisse** - [meurissemax](https://github.com/meurissemax)
