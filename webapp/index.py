from crypt import methods
from flask import Blueprint, render_template, request

index = Blueprint('index',__name__)


@index.route('/')
def home():
    return render_template('index.html')

@index.route('/gpt-2')
def gpt_2():
    return render_template('gpt-2.html')

@index.route('/dolly-3b')
def dolly_3b():
    return render_template('dolly-3b.html')

@index.route('/stable-diffusion')
def stable_diffusion():
    return render_template('stable-diffusion.html')