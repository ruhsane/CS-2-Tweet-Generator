import sys
from flask import Flask, render_template, request
import Markov_Chain2


app = Flask(__name__)

app.config.update(
    DEBUG=True,
    # TEMPLATES_AUTO_RELOAD=True
)

app.trump_word_list = Markov_Chain2.Markov.words_list_from_file("story.txt")
app.trump_markov = Markov_Chain2.Markov.model(app.trump_word_list)

@app.route('/')
def trumpTweet():

    app.trump_string = Markov_Chain2.Markov.result_sentence(app.trump_markov)
    print(app.trump_string)

    return render_template("home.html", sentence = app.trump_string)

@app.route('/api', methods=['POST'])
def api():
    req_data = request.get_json()
    source = req_data['content']

    app.word_list = Markov_Chain2.Markov.words_list_from_string(source)
    app.markov = Markov_Chain2.Markov.model(app.word_list)
    app.string = Markov_Chain2.Markov.result_sentence(app.markov)
    # print(app.string)
    return app.string

    # return render_template("home.html", sentence = app.string)


if __name__ == '__main__':
    app.run()
