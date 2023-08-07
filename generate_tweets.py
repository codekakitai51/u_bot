import os
import boto3
import markovify
import tweepy

# download file from AWS S3
s3_client = boto3.client('s3',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'],
    region_name='us-west-2'  # specify your region
)

s3_client.download_file('splitedtextforubot', 'splitted.txt', 'splitted.txt')

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
