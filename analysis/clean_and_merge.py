import pandas as pd

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

if __name__ = '__main__':
    print('Processing Trump Tweets')

    trump = pd.read_csv('trump_tweets/TrumpTweets.csv')
    trump['text'] = trump['text'].apply(clean_tweet_text)
    
    trump = trump[trump['text'] != '']
    trump = trump[trump['text'].notnull()]
    trump = trump[(trump['is_retweet'] == 'false') | (trump['is_retweet'] == 'true')]
    trump = trump.sample(frac = 1)

    
    print('Processing Control Tweets')

    control = pd.read_csv('control/control_tweets.csv')
