from flask import Flask, request
from flask_cors import CORS
from unchi import Analysis

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
TOKENIZE = Analysis()


@app.route('/')
def main():
  text = request.args.get('text')

  formated_text = ''

  if text != '' and text is not None:
    formated_text = ''.join(TOKENIZE.change_noun(text, 'うんち'))

  return {"formatted_text": formated_text}


if __name__ == "__main__":
  app.run(debug=True)
