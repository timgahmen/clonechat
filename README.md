# Clonechat

Clone all posts from the history of a Telegram Channel/Group to another Channel/Group.

Secure backup. Saves and protects the posts in the destination chat from possible deletion of posts from the source chat.

>> [Versão em Português](README_ptbr.md)

## Settings
- Run `update_libs.bat` file to update dependencies
- Register your telegram API access credentials in the `credentials.py` file

## USE

### via command line

Command: 
python3 clonechat.py --orig={chat_id of source channel/group} --dest=-{chat_id of destination channel/group}

Example: 
python3 clonechat.py --orig=-100222222 --dest=-10011111111

If you want to clone via bot:

Example: 
python3 clonechat.py --orig=-100222222 --dest=-10011111111 --mode=bot

If you want to continue a cloning task instead of starting. Useful for updating a cloned channel or resuming a previously interrupted cloning task:

Enter whether you want to start a new clone or continue a cloning you started previously

    Type 1 for new cloned
    or 2 to continue

Example: python3 clonechat.py --orig=-100222222 --dest=-10011111111 --new=2

### Via menu in terminal

You need to have the api_id and api_hash of your account before you can run clonechat.

    python3 clonechat.py

    Enter the chat_id of the source channel/group. If the ctrl+v doesn't work, right-click on the terminal

    Confirm with [ENTER]

    Enter the chat_id of the target channel/group

    Confirm with [ENTER]

    From the menu of choosing file types
        Enter a file filter option
        If you want to clone all files, type zero
        You can select multiple options by separating them with commas. 1,3 to clone only photos and documents.

    Enter whether you want to start a new clone or continue a cloning you started previously
        Type 1 for new cloned
        or 2 to continue

    Confirm with [ENTER]

    The first time you use it, you'll need to authenticate a connection to Telegram. But it will only be the first time! And then never again. :) Authenticating is simple, follow the steps:

        "Enter phone number or bot token:"

        This message will appear asking for your phone number in international format.
        Enter your phone number with prefix +55 for the case of a Brazilian telephone number, followed by the local area code and its telephone number.
            Example: For a telephone in São Paulo, with area code 11, something like the following should be entered: +5511995429405
        In the message asking if the number is correct, type y.
        A code will be sent to your telegram, which you must enter in the terminal.
        Finally, if you have '2-factor security' (2fa) enabled on your account, you will be asked for your password.
        By running the exec_clonechat.bat, you will be asked for your api_id and api_hash. You only need to inform them once, as the other connections will be made by a session file that will be created in the clonechat folder.


### Finalization

- Delete the `posted.json` file when done cloning.

Note: If this file is not deleted, the next time you run the script the cloning will continue where it left off.

## FAQ

### How to get the chat_id of a channel or group

There are several ways to get the chat_id of a channel. We will show two of them:
- Using telegram client [Kotatogram](https://kotatogram.github.io/download/):
  - Access the channel description screen
  - Copy the `chat_id` that appears below the channel name
- Using Find_TGIDbot bot:
  - Access the bot window [@Find_TGIDbot](http://t.me/Find_TGIDbot) and launch it
  - Forward any channel post to this bot
  - The bot will reply with the message sender ID. In this case, the channel ID.
- Copy the `chat_id` (including the minus sign). It is worth mentioning that channels start with the number '-100'.

### How to generate telegram API access credentials?

- View this video: https://www.youtube.com/watch?v=8naENmP3rg4
