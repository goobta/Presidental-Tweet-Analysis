from NaiveBayes import NaiveBayes
import json

def load_saved_model():
    def convert_to_bool(d):
        new_dict = {}
        new_dict[True] = d['True']
        new_dict[False] = d['False']
        return new_dict

    with open('p_c.json', 'r') as fh:
        p_c = convert_to_bool(json.load(fh))

    with open('B.txt', 'r') as fh:
        B = int(fh.read())

    with open('total_counts.json', 'r') as fh:
        total_counts = convert_to_bool(json.load(fh))

    with open('freqs.json', 'r') as fh:
        freqs = convert_to_bool(json.load(fh))

    nb = NaiveBayes(p_c_=p_c, B_=B, t_c=total_counts, freqs_=freqs)
    return nb
