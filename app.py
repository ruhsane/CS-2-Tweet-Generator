from flask import Flask
from Markov_Chain2 import Markov

app = Flask(__name__)

app.word_list = Markov.words_list("/Users/ruhsane/dev/courses/cs1.2/CS-2-Tweet-Generator/story.txt")
app.markov = Markov.model(app.word_list)
# print(data_structure)

@app.route('/')
def hello_world():
    return Markov.result_sentence(app.markov)
