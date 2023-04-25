#!/usr/bin/env python3
from flask import Flask
from flask_babel import Babel
from flask import render_template, request


class Config:
    """get_locale function with the
       babel.localeselector decorator.
    """
    LANGUAGES = ["en", "fr" ]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route('/')
def hello(name=None) -> str:
    return render_template('2-index.html', name=name)


@babel.localeselector
def get_locale():
    """determine the best match
       with our supported languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)