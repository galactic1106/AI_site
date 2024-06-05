# siccome c'è un file chiamato __inti__.py in webapp
# quando viene importata la directory che lo contiene
# verranno eseguite tutte funzioni contenute in esso
from webapp import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
