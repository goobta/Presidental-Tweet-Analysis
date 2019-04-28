from NaiveBayes import NaiveBayes
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv('merged.csv')

    nb = NaiveBayes()
    nb.fit(data['text'], data['is_trump'])

    supports = nb.freqs
    tc = nb.total_counts

    trump_supports = supports[True]
    control_supports = supports[False]

    words = set(trump_supports.keys()) | set(control_supports.keys())

    relative_probs = []
    for word in words:
        if word in trump_supports and word in control_supports:
            trump_prob = trump_supports[word] / tc[True]
            control_prob = control_supports[word] / tc[True]

            relative_probs.append([word, trump_prob - control_prob])

    sort = reversed(sorted(relative_probs, key=lambda x: x[1]))
    df = pd.DataFrame(sort, columns=['Word', 'RelativeProb'])
    df.to_csv('relative_probs.csv')
