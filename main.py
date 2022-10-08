from vkbottle.bot import  Bot, Message
import sqlite3

bot = Bot("vk1.a.M-_rJt9REpV2SACrssaTq0FeXz_2Hlk3KRxbvqzNsulnTbTffgZlidVIzM-X2_ZlMsyXkQ4ojTb9Roqrzw-zFmqkOWz2dtjjqGpsXvmjK4rMYflcmVkKQJ3rY-wTYUwGMSSbK0OPv8SbfbySvLS9FLH83iOEuSiHY3pmTVJakxMVW15pNPc9lme5p0h9a0Wv")

db = sqlite3.connect("root.sqlite")
cursor = db.cursor()


db.commit()

@bot.on.message(text="1")
async def start_handler(message: Message):
    if 1:
        await message.answer("тупой {}".format(cursor.fetchall()[-1][0]))
    else:
        await message.answer("хэй бой")

bot.run_forever()
