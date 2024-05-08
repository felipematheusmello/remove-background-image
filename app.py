from flask import Flask

from .routes import bp_bkgd

app = Flask(__name__)
app.register_blueprint(bp_bkgd)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5100)