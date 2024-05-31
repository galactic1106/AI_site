from flask import Blueprint, render_template, request
from dolly_3b import prompt_dolly_3b
index = Blueprint('index',__name__)


@index.route('/')
def home():
    return render_template('index.html')

@index.route('/gpt-2')
def gpt_2():
    return render_template('gpt-2.html')

@index.route('/dolly-3b',methods=['GET','POST'])
def dolly_3b():
    data= request.form

    #se non c'è un prompt
    if(len(data.get('prompt').strip())<0):
        return render_template('dolly-3b.html')
    
    AI_response=prompt_dolly_3b(data.get('prompt'))
    return render_template('dolly-3b.html',AI_response=AI_response)

@index.route('/stable-diffusion')
def stable_diffusion():
    return render_template('stable-diffusion.html')