import os
import tweepy

api_key = os.environ.get('TWITTER_CONSUMER_KEY')
api_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

with open('current_tweet', 'r') as file:
    thisTweet = file.read()

print(thisTweet)

client.create_tweet(text=thisTweet)

