from flask import Flask, send_from_directory

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir une route et sa fonction de gestion
@app.route('/<path:path>') 
def hello(path):
    return send_from_directory('static',path)

# Lancer le serveur Flask
if __name__ == '__main__':
    app.run()
