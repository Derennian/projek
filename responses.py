import random
from datetime import datetime

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'hey there mang'

    if p_message == 'roll':
        return str(random.randint(1,6))

    if p_message == 'roll 12':
        return str(random.randint(1, 12))

    if p_message == 'igs passwordnya?':
        return 'the first choice to the best future'

    if p_message == 'lagu mars igs?':
        return 'https://youtu.be/HM1BN2Qm8Bo?si=6vwyRaXgIZ5D447c'

    if p_message == 'siapo?':
        return 'NANYO!?'

    if p_message == '!help':
        return " 'This is a help message that you can modify lang.'"

    if p_message == 'regan':
        return 'peak silber 1 xixixixixi'

    if p_message == '!timestamp':
        timestamp = datetime.now()
        a = timestamp.strftime('%H:%M:%S')
        return a

        if p_message == '!google igs website':
        return 'here is the site that you would like to search : https://belajar-online.ignatiusglobal.sch.id/login'

    if p_message == '!google youtube':
        return 'here is the site that you would like to search : https://www.youtube.com/'

    if p_message == "!google netflix":
        return 'here is the site that you would like to search : https://www.netflix.com/browse'

    if p_message == "!google spotify":
        return 'here is the site that you would like to search : https://open.spotify.com/'

    bot = commands.Bot(command_prefix='!')

    @bot.event


    async def on_ready():
        print(f'Logged in as {bot.user.name}')

    @bot.command()
    async def google(ctx, *, query):
        async with ctx.typing():
            results = []

            async with async_timeout.timeout(10):
                for result in search(query, "num=5", "stop=5", "pause=2.0"):
                    results.append(result)

            response = "\n".join(results)
            await ctx.send(f"Search results for '{query}':\n{response}")

    bot.run('token')
    
    return "I dont know what you said broski"
