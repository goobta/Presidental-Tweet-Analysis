import pandas as pd
import numpy as np
import string
import re

TRAIN_RATIO = .7

def clean_tweet_text(tweet):
    try:
        tweet = re.sub(r'\\\'9[0-9]', '', tweet)
        tweet = tweet.translate(str.maketrans('', '', string.punctuation))
        words = tweet.split(' ')

        for index, word in enumerate(words):
            if 'https' in word:
                del words[index]

        return ' '.join(words)

    except:
        return None

if __name__ == '__main__':
    data_raw = pd.read_csv("TrumpTweets.csv")
    data_raw['text'] = data_raw['text'].apply(clean_tweet_text)
    
    data = data_raw[data_raw['text'] != '']
    data = data[data['text'].notnull()]
    data = data[(data['is_retweet'] == 'false') | (data['is_retweet'] == 'true')]
    data = data.sample(frac = 1)

    data = data.reset_index(drop=True)
    data.to_csv('trump_with_rts_clean.csv')

    no_rts = data[data['is_retweet'] == 'false']
    no_rts.to_csv("trump_clean.csv")
