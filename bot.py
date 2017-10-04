import praw

#Log In
print('Logging in...')
reddit = praw.Reddit('bot1', user_agent =  'bot1 user agent') #TODO Password from CMD praw_password=not_my_password python my_script.py
print('Logged in as ' + str(reddit.user.me()))

#Subreddit
print('Connecting...') 
subreddit = reddit.subreddit('SteamTradingCards')
print('Connected to ' + subreddit.title)         
