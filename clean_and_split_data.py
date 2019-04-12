import pandas as pd
import numpy as np

def clean_tweet_text(tweet):
    words = tweet.split(' ')

    for index, word in enumerate(words):
        if 'https://' in word:
            del words[index]

    return ' '.join(words)

if __name__ == '__main__':
    data_raw = pd.read_csv("TrumpTweets.csv")
    no_rts = data_raw[data_raw['is_retweet'] == 'false']

    no_rts['text'] = no_rts['text'].apply(clean_tweet_text)
