from replchat_plus import bot

client = bot.Bot(username = 'replchat+ test')

# Commands
def greet():
    client.message('bruh')

client.Commands.on_user_join = greet

client.run()