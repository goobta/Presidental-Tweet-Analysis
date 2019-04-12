from flask import Flask, request, send_from_directory, render_template
import os.path
import random
import string
import os 

app = Flask(__name__, static_url_path='')
app.config['TEMPLATES_AUTO_RELOAD'] = True #TODO remove when done

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
