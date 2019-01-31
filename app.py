import sys
from flask import Flask
from flask import render_template

import Markov_Chain2

print('Python version: ' + sys.version)

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True
)

app.word_list = Markov_Chain2.Markov.words_list("story.txt")
app.markov = Markov_Chain2.Markov.model(app.word_list)

@app.route('/')
def hello_world():
    # return
    string = Markov_Chain2.Markov.result_sentence(app.markov)
    return render_template("home.html", sentence = string)

if __name__ == '__main__':
    hello_world()
