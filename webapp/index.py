from flask import Blueprint, render_template, request
from flask import *
import prompt_toolkit
from .dolly_3b import prompt_dolly_3b

index = Blueprint("index", __name__)


def format_conv(conversation):
    out = ""
    for msg in conversation:
        out += msg + " "


@index.route("/")
def home():
    return render_template("index.html")


@index.route("/gpt-2")
def gpt_2():
    return render_template("gpt-2.html")


@index.route("/dolly-3b", methods=["GET", "POST"])
def dolly_3b():

    AI_response = ""
    data = request.form
    prompt = data.get("prompt")

    # se non c'è un prompt
    if prompt == None:
        return render_template("dolly-3b.html")
    if len(prompt.strip()) < 0:
        return render_template("dolly-3b.html")

    AI_response = prompt_dolly_3b(data.get("prompt"))
    conversation = data.get("conversation")
    if conversation == None:
        conversation = ""
    else:
        conversation=conversation.split(' ')
        for str in conversation:
            if str.strip=='':
                conversation.remove('')
    
    return render_template("dolly-3b.html", conversation=conversation)


@index.route("/stable-diffusion")
def stable_diffusion():
    return render_template("stable-diffusion.html")
