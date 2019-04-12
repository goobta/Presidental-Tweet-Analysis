import pandas as pd
import numpy as np
import string
import re

TRAIN_RATIO = .7

def clean_tweet_text(tweet):
    tweet = re.sub(r'\\\'9[0-9]', '', tweet)
    tweet = tweet.translate(str.maketrans('', '', string.punctuation))
    words = tweet.split(' ')

    for index, word in enumerate(words):
        if 'https' in word:
            del words[index]

    return ' '.join(words)

if __name__ == '__main__':
    data_raw = pd.read_csv("TrumpTweets.csv")
    no_rts = data_raw[data_raw['is_retweet'] == 'false']
    no_rts['text'] = no_rts['text'].apply(clean_tweet_text)

    no_rts.to_csv("trump_clean.csv")
