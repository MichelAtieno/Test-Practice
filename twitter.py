import tweepy, csv
from dotenv import load_dotenv
load_dotenv()

import os
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.verify_credentials()

##Search for Acute Encephalitis Syndrome
# search = api.search(q="Acute Encephalitis Syndrome", lang="en", rpp=100, count=100)

# for tweet in search:
#     print(tweet.text, tweet.created_at, tweet.user.location )

# print(len(search))

## Task: Is to get at least 1000 tweets from the twitter API and save it
## To a CSV file

file_out = open("tweets.csv", "w+", encoding="utf-8")
writer = csv.writer(file_out)

i=0
writer.writerow(["created_at", "screen_name", "text"])
for item in tweepy.Cursor(api.search, q="Encephalitis Syndrome").items(100):
    tweet = []
    print("Adding item",i, item.id)
    i+=1
    tweet.append(item.created_at)
    tweet.append(item.user.screen_name)
    tweet.append(item.text)
    writer.writerow(tweet)
