from multiprocessing.dummy import Pool as ThreadPool

class NaiveBayes:
    def __init__(self, THREADS = 8):
        self.p_c = None
        self.freqs = None
        self.threads = THREADS

    def fit(self, x, y):
        counts = x.apply(lambda x: len(x.split(' ')))
        N = counts.sum()

        classes = y.unique()
        self.p_c = {}
        self.freqs = {}

        for c in classes:
            indices = y == c

            n_c = counts[indices].sum()
            self.p_c[c] = n_c / N

            pool = ThreadPool(self.threads)
            freqs = pool.map(self._word_freq_for_sent, x[indices])
            
            pool.close()
            pool.join()

            class_freqs = {}
            for freq in freqs:
                for word, count in freq.items():
                    if word in class_freqs:
                        class_freqs[word] += 1
                    else:
                        class_freqs[word] = 1
            
            self.freqs[c] = class_freqs

    def predict(self, x):
        def predict_singular(sentence):
            for c, freq in self.freqs.items():
                class_prob = self.p_c[c]

                for word in sentence.split(" "):
                    pass

        return x.apply(predict_singular)


    def _word_freq_for_sent(self, sent):
        freqs = {}
        
        for word in sent.split(' '):
            if word in freqs:
                freqs[word] += 1
            else:
                freqs[word] = 1

        return freqs
