import tweepy
#these are found on your twitter developer page. If you do not have one you will need to create one.

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

def get_usr_recent_tweets():
	#this is the function that will get the users tweets.
	print("Enter the username of the person who's tweets you want to see:")
	screen_name = input('--> ')
	user_tweets = api.user_timeline(screen_name)
	for tweet in user_tweets:
		print(tweet.text)
		print("")
		print("---------------------------------------------")
		print("")

if __name__ == '__main__':

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	user = api.me()
	
	get_usr_recent_tweets()