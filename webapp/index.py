from flask import Blueprint, render_template, request
from flask import *
from .gpt_2 import init_gpt_2, prompt_gpt_2
from .dolly_3b import prompt_dolly_3b

index = Blueprint("index", __name__)
init_gpt_2=True
gpt_2_ai=init_gpt_2()

init_dolly_3b=False
if init_dolly_3b: prompt_dolly_3b('')

@index.route("/")
def home():
    return render_template("index.html")


@index.route("/gpt-2")
def gpt_2():
    return render_template("gpt-2.html")

@index.route("/guida")
def guida():
    return render_template("guida.html")


@index.route("/dolly-3b", methods=["GET", "POST"])
def dolly_3b():
    AI_response = ""
    q_a = []
    data = request.form
    prompt = data.get("prompt")
    # se non c'è un prompt
    if prompt == None:
        return render_template("dolly-3b.html", q_a=q_a)
    if len(prompt.strip()) < 0:
        return render_template("dolly-3b.html", q_a=q_a)


    AI_response = prompt_dolly_3b(data.get("prompt"))
    AI_response = 'PLACEHOLDER'
    try: q_a = eval(data.get("q_a"))
    except: q_a = []
    
    q_a.append({"q": prompt, "a": AI_response})
#    for qa in q_a:
#        print(qa["q"])
#        print(qa["a"])
    return render_template("dolly-3b.html", q_a=q_a)


@index.route("/stable-diffusion")
def stable_diffusion():
    return render_template("stable-diffusion.html")
