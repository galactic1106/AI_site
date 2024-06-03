from flask import Blueprint, render_template, request
import prompt_toolkit
from .dolly_3b import prompt_dolly_3b
index = Blueprint('index',__name__)

def make_conversation_html(conversation):
	conversation_html=''
	part_1='<div class="d-flex flex-row justify-content-end mb-3"><div class="p-3 py-2 bg-info rounded-start-4 text-black text-end text-wrap text-break" style="max-width: 70%;"><h5>User</h5><span>'
	part_2='</span></div></div><div class="d-flex flex-row justify-content-start mb-3"><div class="p-3 py-2 bg-info-subtle rounded-end-4 text-start text-wrap text-break" style="max-width: 70%;"><h5>Dolly 3b</h5><span>'
	part_3='</span></div></div>'
	for i in range (0, len(conversation),2):
		prompt= conversation[i]
		AI_response=conversation[i+1]
		
		conversation_html+=(part_1+prompt+part_2+AI_response+part_3)
	return conversation

def format_conv(conversation):
	out=''
	for msg in conversation: out+=msg+' '

@index.route('/')
def home():
    return render_template('index.html')

@index.route('/gpt-2')
def gpt_2():
    return render_template('gpt-2.html')

@index.route('/dolly-3b',methods=['GET','POST'])
def dolly_3b():
	
    
	AI_response=''
	data= request.form
	prompt= data.get('prompt')

	#se non c'è un prompt
	if prompt==None:
		return render_template('dolly-3b.html')
	if len(prompt.strip())<0 :
		return render_template('dolly-3b.html')
	
	AI_response=prompt_dolly_3b(data.get('prompt'))
	
	conversation=data.get('conversation').split(' ')
	conversation.append(prompt)
	conversation.append(AI_response)
	conversation_html=make_conversation_html(conversation)
	conversation= format_conv(conversation)
	return render_template('dolly-3b.html', conversation=conversation, conversation_html=conversation_html)

@index.route('/stable-diffusion')
def stable_diffusion():
    return render_template('stable-diffusion.html')