#siccome c'è un file chiamato __inti__.py in webapp
#quando viene importata la directory che lo contiene 
#verranno eseguite tutte funzioni contenute in esso 
from webapp import create_app 
from webapp.dolly_3b import prompt_dolly_3b

app = create_app()

if __name__=='__main__':
    app.run()