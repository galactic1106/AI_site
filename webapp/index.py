from flask import Blueprint, render_template

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