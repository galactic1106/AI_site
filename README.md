# AI_site
sito contenete un IA creato per un compito scolastico

video riferimento: "https://youtu.be/dam0GPOAvVI?si=bUTpxU-v4zExO5jk"
nella cartella static vanno immagini, javascript, css...

lista moduli(si installano con "pip install"):
	flask
	pyngrok

	torch

	accelerate
	transformers

	diffusers
	scipy
	ftfy

	"jax[cuda12_local]==0.4.23" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html


__init__.py:
	'run_with_ngrok': server per creare un tunnel ngrok per accedere all sito.

index.py:
	'flag_dolly_3b': serve per inizializzare Dolly 3b all lancio dell'app.
	'flag_gpt_2': serve per inizializzare GPT-2 all lancio dell'app.
	'flag_stable_diffusion': serve per inizializzare stable diffusion all lancio dell'app.

