from multiprocessing.dummy import Pool as TheadPool
import pandas as pd
import datetime
import got
import sys

reload(sys)   
sys.setdefaultencoding('utf-8')

THREADS = 16
UNIT_TWEETS = 1000
CHUNK_LENGTH = 30

def download_tweets(bounds):
    from_date = bounds[0]
    to_date = bounds[1]

    print("Start from " + from_date + ' to ' + to_date)

    criteria = got.manager.TweetCriteria().setQuerySearch('a OR the').setSince(from_date).setUntil(to_date).setTopTweets(True).setMaxTweets(1000)
    
    tweets = got.manager.TweetManager.getTweets(criteria)
    df = pd.DataFrame([t.__dict__ for t in tweets])

    print("End from " + from_date + ' to ' + to_date)

    return df


if __name__ == '__main__':
    time_to_str = lambda t: t.strftime("%Y-%m-%d")

    bounds = []

    end = datetime.datetime.now() - datetime.timedelta(days=CHUNK_LENGTH)
    curr = datetime.datetime(2015, 1, 1)

    while curr < end:
        new = curr + datetime.timedelta(days=CHUNK_LENGTH)

        bounds.append([time_to_str(curr), time_to_str(new)])
        curr = new
    
    pool = TheadPool(4)
    tweets = pool.map(download_tweets, bounds)

    pool.close()
    pool.join()

    df = pd.concat(tweets).reset_index(drop=True)
    df.to_csv('control_tweets.csv', index=False)
