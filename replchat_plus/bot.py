import socketio

sio = socketio.Client()

# Error classes
class ClientBanned: pass
class ClientKicked: pass

url = 'https://replchat.vapwastaken.repl.co'

def emit(content):
    global sio
    sio.emit('chat message', {'message': content})

class Bot:
    '''
    Class for initializing the bot.

    Parameters:
    username (str, required): the username the bot will use in replchat
    command_prefix (str, required): the prefix for bot commands
    '''
    def __init__(self, username, command_prefix):
        self.username = username
        self.command_prefix = command_prefix

    def message(content):
        '''
        Send a message to replchat via the bot
        '''
        emit(content)

    class Commands:
        def on_bot_join():
            pass

        def on_user_join(data):
            pass

        def on_user_leave(data):
            pass

        def on_message(data):
            pass


# Socketio stuff
@sio.event()
def connect():
    Bot.Commands.on_bot_join()

@sio.on('chat message')
def chat_message(data):
    Bot.Commands.on_message(data)

@sio.on('joined')
def joined(data):
    Bot.Commands.on_user_join(data)

@sio.on('left')
def left(data):
    Bot.Commands.on_user_leave(data)

# Kicks/Bans
@sio.on('admin.kick')
def admin_kick(data):
    sio.disconnect()
    raise ClientKicked(f'\n\nThe client {Bot.username} was kicked from replchat')

@sio.on('banned')
def banned(data):
    sio.disconnect()
    raise ClientBanned(f'\n\nThe client {Bot.username} was banned from replchat.')

@sio.event()
def debug(code):
    if code == 'REQUIRES_IDENTIFY':
        sio.emit('identify', Bot.username + ' [BOT with replchat+]')

def run():
    '''
    Connect the bot to replchat!
    '''
    sio.connect(url, headers = {'X-Replit-User-Name': Bot.username})
    sio.wait()