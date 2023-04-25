from flask import Flask
from flask_babel import Babel
from flask import render_template


class Config:
    LANGUAGES = ["en", "fr" ]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

@app.route('/')
def hello(name=None) -> str:

    return render_template('1-index.html', name=name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)