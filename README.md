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

Each bot must log in to a Facebook account and interact with a Messenger conversation.

* Account IDs are requested when running the program and therefore never appear in a file.
* The type of conversation (conversation with a person or group conversation) and the ID of the conversation must be defined in the `config.py` file before the use of the bots. The conversation ID can be found in the URL of the conversation or via external tools.

When the file `config.py` has been configured, all that remains is to launch a bot with the command :
```
python3 /path/to/some-bot.py
```

### Additionnal libraires

Some bots use additional Python libraries. Here is the complete list of all the additional libraries uses :

* google

## Author

* **Maxime Meurisse** - [meurissemax](https://github.com/meurissemax)
