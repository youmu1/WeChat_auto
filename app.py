import json

from wxpy import *
bot = Bot(cache_path=True)
# friend_total = bot.friends().stats_text()
# print(friend_total)
all_friends = bot.friends(update=True)
print(all_friends.search())