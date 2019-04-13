from multiprocessing.dummy import Pool as ThreadPool

class NaiveBayes:
    def __init__(self, THREADS = 8):
        self.threads = THREADS

        self.p_c = None
        self.B = None
        self.total_counts = None
        self.freqs = None

    def fit(self, x, y):
        counts = x.apply(lambda x: len(x.split(' ')))
        N = counts.sum()

        classes = y.unique()
        self.p_c = {}
        self.freqs = {}
        self.total_counts = {}

        unique_words = set()

        for c in classes:
            indices = y == c

            n_c = counts[indices].sum()
            self.p_c[c] = n_c / N

            pool = ThreadPool(self.threads)
            freqs = pool.map(self._word_freq_for_sent, x[indices])
            
            pool.close()
            pool.join()

            class_freqs = dict()
            class_words = 0
            for freq in freqs:
                for word, count in freq.items():
                    if word in class_freqs:
                        class_freqs[word] += 1
                    else:
                        class_freqs[word] = 1
                        unique_words.add(word)

                    class_words += 1
            
            self.freqs[c] = class_freqs
            self.total_counts[c] = class_words

        self.B = len(unique_words)


    def predict_singular(self, sentence):
        probs = {}

        for c, freq in self.freqs.items():
            class_prob = self.p_c[c]

            for word in sentence.split(" "):
                if word in self.freqs[c]:
                    t_c = self.freqs[c][word]
                else:
                    t_c = 0

                class_prob *= (t_c + 1) / (self.total_counts[c] + self.B)

            probs[c] = class_prob

        best_class = None
        best_prob = 0
        for c, prob in probs.items():
            if prob > best_prob:
                best_prob = prob
                best_class = c

        return best_class

    def predict(self, x):
        return x.apply(predict_singular)


    def _word_freq_for_sent(self, sent):
        freqs = {}
        
        for word in sent.split(' '):
            if word in freqs:
                freqs[word] += 1
            else:
                freqs[word] = 1

        return freqs