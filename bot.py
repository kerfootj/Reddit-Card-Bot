# Created By Joel Kerfoot
# 02/10/2017
# Python 2.7
# Reddit Post Bot v0.2

import praw
import config
import time
import re

n = 1

def bot_login():
	print('Logging in...')
	reddit = praw.Reddit('bot1', user_agent =  'bot1 user agent') #TODO Password from CMD praw_password=not_my_password python my_script.py
	print('Logged in as ' + str(reddit.user.me()))
	return reddit
	
def run_bot(reddit):
	
	global n 
	print(config.Spacer + '\n#' + str(n) + '\n' + config.Spacer + '\nSubmitting New Post...')
	n+=1
	subreddit = reddit.subreddit('SteamTradingCards')
	submission = subreddit.submit(config.Title, config.Body)
	print('Post Submitted\nSleeping for 45 minutes...')
	time.sleep(2700)
		
	print('Deleting Old Post...\n\n')
	submission.delete()
	
reddit = bot_login()
while True:
	run_bot(reddit)

