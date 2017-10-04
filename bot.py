# Created By Joel Kerfoot
# 02/10/2017
# Python 2.7
# Reddit Post Bot v0.2

import praw
import config
import time
import re

def bot_login():
	print('Logging in...')
	reddit = praw.Reddit('bot1', user_agent =  'bot1 user agent') #TODO Password from CMD praw_password=not_my_password python my_script.py
	print('Logged in as ' + str(reddit.user.me()))
	return reddit
	
def run_bot(reddit):
	
	print('Submitting Post...')
	subreddit = reddit.subreddit('SteamTradingCards')
	subreddit.submit(config.Title, config.Body)
	print('Post Submitted')
	
	print('Sleeping for 45 minutes...')
	time.sleep(2700)
	
reddit = bot_login()
while True:
	run_bot(reddit)

#Title = 'NEED SUPPLIERS! | [H] 100+ Keys | Aviators Lvlup | Buying 24:1 | Selling 26:1 | Anyone Can Sell!' #TODO get value from CONFIG

#Body1 = "**BUY & SELL**"
#Body2 = "**Everybody can sell! No Whitelist**"
#Botlink = "Bot - http://steamcommunity.com/id/AviatorBot1"
#Grouplink = "Group - http://steamcommunity.com/groups/AviatorLVLUP"
#submission = subreddit.submit(Title, Botlink)

#https://stackoverflow.com/questions/10222642/read-javascript-variables-from-a-file-with-python
