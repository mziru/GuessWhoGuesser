import json

from flask import Flask
from pywebio.input import select
from pywebio.output import put_text, put_image
from pywebio.platform.flask import webio_view

app = Flask(__name__)


def guesser_io():
    with open("guess_who_decision_tree.txt") as file:
        game_tree = json.loads(file.read())

    put_text('Characters: ')
    put_image(src='https://i.redd.it/ad8maaz1wqw21.jpg')
    put_text('')

    while True:
        try:
            put_text('GUESS: ', game_tree['SOLUTION'][0])
            break
        except:
            put_text('ASK: ', game_tree['next_question'])
            response = select(options=[{"label": 'YES', "value": 'YES'},
                                       {"label": 'NO', "value": 'NO'}])
            put_text(response)
            game_tree = game_tree[response]


app.add_url_rule('/', 'webio_view', webio_view(guesser_io),
                 methods=['GET', 'POST', 'OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True)
