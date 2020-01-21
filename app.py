from wxpy import *
bot = Bot(console_qr=1)
friend_total = bot.friends().stats_text()
print(friend_total)