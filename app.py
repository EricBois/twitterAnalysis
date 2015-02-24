import tweepy
import requests
import json

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

searchTerm = raw_input('>>> ')
url = 'http://text-processing.com/api/sentiment/'

auth = tweepy.auth.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

tweets = api.search(q=searchTerm, rpp=100)

for t in tweets:
	#print t.created_at, t.text, "\n"
	data = {'text': t.text}
	r = requests.post(url, data=data)
	binary = r.content
	output = json.loads(binary)
	label = output["label"]
	if label == "neg":
		print t.text