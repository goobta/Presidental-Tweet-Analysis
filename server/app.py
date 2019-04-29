from analysis.NaiveBayes import NaiveBayes
from analysis.nb_utils import load_saved_model
from flask import Flask, request, send_from_directory, render_template
from flask_bootstrap import Bootstrap
import pandas as pd
import os.path
import random
import string
import json
import os 

app = Flask(__name__, static_url_path='')
app.config['TEMPLATES_AUTO_RELOAD'] = True #TODO remove when done
Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

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

        output = {
                'class': str(prediction['Class'][0]),
                'confidence': key_to_string(prediction['Confidence'][0])
                }

        return json.dumps(output)
    else:
        print('Not a post request.')
        return 'NOTAVALIDPATH'



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


