#siccome c'è un file chiamato __inti__.py in webapp
#quando viene importata la directory che lo contiene 
#verranno eseguite tutte funzioni contenute in esso 
from webapp import create_app 
import threading

app = create_app()

if __name__=='__main__':
    on_colab=False
    if on_colab:
        threading.Thread(target=app.run, kwargs={"use_reloader": False}).start()
    else:
        app.run()