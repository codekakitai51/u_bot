import os
import markovify
import tweepy
from gcp_functions import download_blob

# download the file from GCP
download_blob("u-bot-bucket", "gcp-tweets-wakatied.txt", "tweets-wakatied.txt")

# fetch sentences from splitted.txt and generate a random sentence
with open('splitted.txt', 'r', encoding='utf-8') as input_file:
    model = markovify.NewlineText(input_file.read())
    sentence = model.make_sentence()
# remove spaces because the sentence is generated as "-Owakati"
generated_tweet = sentence.replace(" ","")

api_key = os.environ['API_KEY']
api_key_secret = os.environ['API_KEY_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

client.create_tweet(text=generated_tweet)
