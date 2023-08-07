import os
import requests
import re
import MeCab

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


def create_url():
    # Replace with user ID below
    user_id = 1449620846956269575 
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {
            # ↓↓ fetch tweets by selecting end_time ↓↓
            # "end_time":"2023-06-20T00:00:00Z",          
            "max_results":100
            }  

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

# modify texts for MeCab
def preprocess_wordcloud(doc): 
    # removing mentions
    doc = re.sub(r"@(\w+) ", "", doc) 
    # removing URLs
    doc = re.sub(r"http\S+", "", doc)
    # removing retweets
    doc = re.sub(r"(^RT.*)", "", doc, flags=re.MULTILINE | re.DOTALL)
    return doc

# log out to tweets.txt file
def log_in_tweets_text(text):
    with open("tweets.txt", "a+") as file:
            file.seek(0)
            if text not in file.read():
                file.write(text + "\n")

# divide(wakachi) and make a new file
def wakachi_division():   
    input = open('./tweets.txt', 'r', encoding='utf-8') # original tweets data
    output = open('./splitted.txt', 'w', encoding='utf-8') # sentences generated as Owatati

    # using -d option to set the path of dictionary
    mecab = MeCab.Tagger("-Owakati -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd/")

    for line in input.read().split('\n'):
        splittedLine = ' '.join(mecab.parse(line).split())
        output.write(splittedLine)
        output.write('\n')

    input.close()
    output.close()


def main():
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)

    for each_data in json_response["data"]:
        text = preprocess_wordcloud(each_data["text"])
        log_in_tweets_text(text)
    
    wakachi_division()


if __name__ == "__main__":
    main()
