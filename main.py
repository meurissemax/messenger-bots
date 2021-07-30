#!/usr/bin/env python3

###########
# Imports #
###########

from fbchat import FBchatException
from fbchat.models import ThreadType
from getpass import getpass

from simple_interactions import simple_chat as bot # do not change the 'as bot' !


########
# Main #
########

def main(
    username: str = None,
    password: str = None,
    thread_type: str = 'user',
    thread_id: str = None,
    bot_id: str = None
):
    # Credentials
    username = str(input('Email address or username: ')) if username is None else username
    password = getpass() if password is None else password

    # Thread
    thread_types = {
        'user': ThreadType.USER,
        'group': ThreadType.GROUP
    }
    thread_type = thread_types.get(thread_type, ThreadType.USER)

    # Bot
    try:
        # Create the bot
        client = bot.MessengerBot(username, password, thread_type, thread_id)

        print('Connected to Facebook.')

        # Let's the bot does it's job
        client.action()
    except FBchatException:
    	print('Login failed')
    except:
        print('Unknow error')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Bot for Facebook Messenger.'
    )

    parser.add_argument(
        '-username',
        type=str,
        default=None,
        help='Email address or username'
    )

    parser.add_argument(
        '-password',
        type=str,
        default=None,
        help='Password'
    )

    parser.add_argument(
        '-type',
        type=str,
        choices=['user', 'group'],
        default='user',
        help='Thread type'
    )

    parser.add_argument(
        '-id',
        type=str,
        default=None,
        help='Thread id'
    )

    args = parser.parse_args()

    main(
        username=args.username,
        password=args.password,
        thread_type=args.type,
        thread_id=args.id
    )
