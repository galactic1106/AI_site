# AI_site
sito contenete un IA creato per un compito scolastico

video riferimento: "https://youtu.be/dam0GPOAvVI?si=bUTpxU-v4zExO5jk"
nella cartella static vanno immagini, javascript, css...

moduli python:"pip install flask"
modulo per creare il tunnel ngrok:"pip install pyngrok" (necessita di ngrok e di un account apposito)
moduli per l'IA:"pip install torch transformers accelerate" 
(forse non sono tutti e se ad esempio non si vuole usare un IA python tenterà di importare i moduli quindi commentate le righe non necessarie)

__init__.py:
	'run_with_ngrok': server per creare un tunnel ngrok per accedere all sito.

index.py:
	'flag_dolly_3b': serve per inizializzare Dolly 3b all lancio dell'app.
	'flag_gpt_2': serve per inizializzare GPT-2 all lancio dell'app.

