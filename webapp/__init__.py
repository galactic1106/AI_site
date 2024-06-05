from multiprocessing.spawn import import_main_path
from flask import Flask
from flask.templating import *
from pyngrok import ngrok
import os

run_with_ngrok=True

dir_path=os.path.dirname(__file__)
def create_app():
	app = Flask(__name__)

	if run_with_ngrok:			
		# app.config['SECRET_KEY']=''  #chiave per la codifica dell'app

		port = "5000"

		# Open a ngrok tunnel to the HTTP server
		public_url = ngrok.connect(port).public_url
		print(f' * ngrok tunnel "{public_url}" -> "http://127.0.0.1:{port}"')

		# Update any base URLs to use the public ngrok URL
		app.config["BASE_URL"] = public_url

	from .index import index

	app.register_blueprint(index, url_prefix="/")

	if not os.path.exists(dir_path+"/static/img/saved_img"): 
		os.makedirs(dir_path+"/static/img/saved_img")

	return app
