from flask import Blueprint, render_template, request
from flask import *
from PIL import Image
import os

dir_path = os.path.dirname(__file__)
flag_gpt_2 = True
flag_dolly_3b = True
flag_stable_diffusion = True

if flag_gpt_2:
    from .gpt_2 import prompt_gpt_2

    prompt_gpt_2("")

if flag_dolly_3b:
    from .dolly_3b import prompt_dolly_3b

    prompt_dolly_3b("")

if flag_stable_diffusion:
    from .stable_diffusion import prompt_stable_diffusion

    prompt_stable_diffusion("")


index = Blueprint("index", __name__)


@index.route("/")
def home():
    return render_template("index.html")


@index.route("/guida")
def guida():
    return render_template("guida.html")


@index.route("/gpt-2", methods=["GET", "POST"])
def gpt_2():
    AI_response = ""
    q_a = []
    data = request.form
    prompt = data.get("prompt")
    # se non c'è un prompt
    if prompt == None:
        return render_template("gpt-2.html", q_a=q_a)
    if len(prompt.strip()) < 0:
        return render_template("gpt-2.html", q_a=q_a)

    AI_response = prompt_gpt_2(prompt)
    # AI_response = 'PLACEHOLDER'
    try:
        q_a = eval(data.get("q_a"))
        q_a.append({"q": prompt, "a": AI_response})
    except:
        q_a = []

    #    for qa in q_a:
    #        print(qa["q"])
    #        print(qa["a"])
    return render_template("gpt-2.html", q_a=q_a)


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

    AI_response = prompt_dolly_3b(prompt)
    try:
        q_a = eval(data.get("q_a"))
        q_a.append({"q": prompt, "a": AI_response})
    except:
        q_a = []
    #    for qa in q_a:
    #        print(qa["q"])
    #        print(qa["a"])
    return render_template("dolly-3b.html", q_a=q_a)


@index.route("/stable-diffusion", methods=["GET", "POST"])
def stable_diffusion():
    data = request.form
    prompt = data.get("prompt")
    # se non c'è un prompt
    if prompt == None:
        return render_template("stable-diffusion.html")
    if len(prompt.strip()) < 0:
        return render_template("stable-diffusion.html")

    # /home/galactic1106/Documents/GitHub/AI_site/webapp/static/img/openart-image_Fj-iov5i_1716968070034_raw.jpg
    image = prompt_stable_diffusion(prompt=prompt)
    # image = Image.open("./webapp/static/img/openart-image_Fj-iov5i_1716968070034_raw.jpg")

    path = dir_path + "/static/img/saved_img/" + prompt + ".png"
    print(path)
    image.save(path)
    return render_template("stable-diffusion.html", image=prompt + ".png")
