from flask import Flask
import Markov_Chain2

app = Flask(__name__)

app.word_list = Markov_Chain2.Markov.words_list("story.txt")
app.markov = Markov_Chain2.Markov.model(app.word_list)

@app.route('/')
def hello_world():
    return Markov_Chain2.Markov.result_sentence(app.markov)
    return  render_template("home.html", sentence= markov_model.random_walk(15))
