from NaiveBayes import NaiveBayes
import pandas as pd
import numpy as np
import json

if __name__ == '__main__':
    print("Loading Data")
    data = pd.read_csv('merged.csv')

    features = data['text']
    labels = data['is_trump']

    x_train = features.loc[:int(.7 * features.shape[0])]
    y_train = labels.loc[:int(.7 * labels.shape[0])]
    x_test = features.loc[int(.7 * features.shape[0]) + 1:].reset_index(drop = True)
    y_test = labels.loc[int(.7 * labels.shape[0]) + 1:].reset_index(drop = True)

    accuracy = lambda y, y_hat: np.mean(y == y_hat['Class'])

    nb = NaiveBayes()

    print("Training")
    nb.fit(x_train, y_train)

    print("Training accuracy: {}".format(accuracy(y_train, nb.predict(x_train))))
    print("Testing accuracy:  {}".format(accuracy(y_test, nb.predict(x_test))))


    print('Saving NB Classifier')

    def key_to_string(d):
        res = {}
        res['True'] = d[True]
        res['False'] = d[False]

        return res


    with open('p_c.json', 'w') as fh:
        json.dump(key_to_string(nb.p_c), fh)

    with open('B.txt', 'w') as fh:
        fh.write(str(nb.B))

    with open('total_counts.json', 'w') as fh:
        json.dump(key_to_string(nb.total_counts), fh)

    with open('freqs.json', 'w') as fh:
        json.dump(key_to_string(nb.freqs), fh)

