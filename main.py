from vkbottle.bot import Bot, Message
from vkbottle import GroupEventType, GroupTypes, Keyboard, KeyboardButtonColor, Text, Callback
from vkbottle import BaseStateGroup
from models import *

bot = Bot("vk1.a.M-_rJt9REpV2SACrssaTq0FeXz_2Hlk3KRxbvqzNsulnTbTffgZlidVIzM-X2_ZlMsyXkQ4ojTb9Roqrzw-zFmqkOWz2dtjjqGpsXvmjK4rMYflcmVkKQJ3rY-wTYUwGMSSbK0OPv8SbfbySvLS9FLH83iOEuSiHY3pmTVJakxMVW15pNPc9lme5p0h9a0Wv")


class States(BaseStateGroup):
    AWKWARD_STATE = "awkward"
    CONFIDENT_STATE = "confident"
    TERRIFYING_STATE = "terrifying"

@bot.on.private_message(text="Начать")
@bot.on.private_message(payload = {"cmd": "start"})
async def start_handler(message: Message):
    try:
        User.get(vk_id=message.from_id)
        await message.answer("hello")
    except:
        await bot.state_dispenser.set(message.peer_id, States.AWKWARD_STATE)
        await message.answer("Введите название своего поселения: ")
        
bot.run_forever()
