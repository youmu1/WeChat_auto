import json
import re
from wxpy import *

zf = "新年快乐"
bot = Bot(cache_path=True)
# friend_total = bot.friends().stats_text()
# print(friend_total)
all_friends = bot.friends()
# print(all_friends)
i = 0
while all_friends[i]:
    s1 = all_friends[i].name

    s1 = s1 + "," + zf
    print( s1 )

    i = i+1
