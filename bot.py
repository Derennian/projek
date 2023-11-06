import discord
import responses
import datetime

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTE2OTE0NzkwMzY5NzIyNzc5Ng.Gg-V9C.JRpP6aqXvhKUn3b3-MJoefRv61vqBOa23W3jjY'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel}")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

        if user_message == '!timestamp':
            timestamp = datetime.utcnow()
            await message.channel.send(timestamp)
            await message.channel.send(timestamp.strftime("%I:%M %p"))

    client.run(TOKEN)

