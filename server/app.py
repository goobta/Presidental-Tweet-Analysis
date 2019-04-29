from analysis.NaiveBayes import NaiveBayes
from analysis.nb_utils import load_saved_model
from flask import Flask, request, send_from_directory, render_template
from flask_bootstrap import Bootstrap
import pandas as pd
import textstat
import os.path
import random
import string
import json
import os 

app = Flask(__name__, static_folder='static')
app.config['TEMPLATES_AUTO_RELOAD'] = True #TODO remove when done
Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/reading_level', methods=['POST'])
def reading_level():
    if request.method != 'POST':
        print('Not a post request')
        return 'NOTAVALIDPATH:'

    sentence = request.get_json()['sentence']
    level = textstat.flesch_reading_ease(sentence)

    return json.dumps({'level': level})


@app.route('/predict', methods=['POST'])
def predict():
    def key_to_string(d):
        res = {}
        res['True'] = d[True]
        res['False'] = d[False]

        return res

    if(request.method == 'POST'):
        nb = load_saved_model('../analysis/')
        
        query = request.get_json()['sentence']
        print('Request to predict {}'.format(query))

        sentence = pd.Series([query])
        prediction = nb.predict(sentence)

        trump_confidence = prediction['Confidence'][0][True] / (prediction['Confidence'][0][True] + prediction['Confidence'][0][False])

        relative_probs = pd.read_csv('../analysis/relative_probs.csv')

        word_confidences = []
        for word in set(query.split(' ')):
            row = relative_probs[relative_probs['Word'] == word]

            if row.shape[0] != 0:
                influence = row['RelativeProb'].values[0]
            else:
                influence = 0
            
            word_confidences.append({
                'label': word, 
                'y': influence
                })

        output = {
                'trump_confidence': trump_confidence, 
                'word_confidences': word_confidences,
                'readability': prediction['Readability'][0]}

        return json.dumps(output)
    else:
        print('Not a post request.')
        return 'NOTAVALIDPATH'



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


