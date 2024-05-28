from flask import Flask, app
import os
from flask.templating import *
from pyngrok import ngrok


def create_app():
    app = Flask(__name__)
    # app.config['SECRET_KEY']=''  #chiave per la codifica dell'app

    port = "5000"

    render_template_string
    # Open a ngrok tunnel to the HTTP server
    public_url = ngrok.connect(port).public_url
    print(f' * ngrok tunnel "{public_url}" -> "http://127.0.0.1:{port}"')

    # Update any base URLs to use the public ngrok URL
    app.config["BASE_URL"] = public_url

    from .index import index

    app.register_blueprint(index, url_prefix="/")

    return app