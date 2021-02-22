import tweepy

consumer_key = "Y0HnPFqOLaBt9H6rGCq5e6hd5"
consumer_secret = "dwqrD2j7rDhcAuUfC4AR9WvbDLE1jhp0DOdXrSrDg3oeqxgDie"

access_token = "359234637-axnhFKE5l9NJfJ7Z1q0rhLQ3Wtbwj4U8lrP0DYVm"
access_token_secret = "qpJGmSVJxvMgLdoAdSq2WJw4zM542J0yWRIBX6atonfU3"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

api.verify_credentials()

##Search for Acute Encephalitis Syndrome
search = api.search(q="Acute Encephalitis Syndrome", lang="en", rpp=100, count=100)

print(search)