from NaiveBayes import NaiveBayes
import pandas as pd
import numpy as np

if __name__ == '__main__':
    print("Loading Data")
    data = pd.read_csv('trump_with_rts_normalized.csv')

    features = data['text']
    labels = data['is_retweet']

    x_train = features.loc[:int(.7 * features.shape[0])]
    y_train = labels.loc[:int(.7 * labels.shape[0])]
    x_test = features.loc[int(.7 * features.shape[0]) + 1:].reset_index(drop = True)
    y_test = labels.loc[int(.7 * labels.shape[0]) + 1:].reset_index(drop = True)

    accuracy = lambda y, y_hat: np.mean(y == y_hat)

    nb = NaiveBayes()

    print("Training")
    nb.fit(x_train, y_train)

    print("Training accuracy: {}".format(accuracy(y_train, nb.predict(x_train))))
    print("Testing accuracy:  {}".format(accuracy(y_test, nb.predict(x_test))))
