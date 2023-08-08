import os
import csv
from datetime import datetime
import tweepy

api_key = os.environ.get('TWITTER_CONSUMER_KEY')
api_secret = os.environ.get('TWITTER_CONSUMER_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Get the current date in the format YYYYMMDD
current_date = datetime.now().strftime('%Y%m%d')

# Get the current meridian (AM or PM)
current_meridian = datetime.now().strftime('%p')

# Initialize thisTweet to None
thisTweet = None

# Read the CSV file
with open('tweets.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['DATE'] == current_date and row['MERIDIAN'] == current_meridian:
            thisTweet = row['TWEET']
            break

# Check if thisTweet is None and handle it
if thisTweet is not None:
    client.create_tweet(text=thisTweet)
else:
    print("No matching tweet found for the current date and meridian.")



