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

    return "I dont know what you said broski"
