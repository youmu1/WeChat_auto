import json
import re

from wxpy import *
bot = Bot(cache_path=True)
# friend_total = bot.friends().stats_text()
# print(friend_total)
all_friends = bot.friends(update=True)
# print(all_friends.search())
# print(all_friends[1])
for i in all_friends:
    s1 = all_friends[i]
    re.split(s1,r'[:>]')
    print(s1[1])