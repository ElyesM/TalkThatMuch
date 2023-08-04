from flask import Flask
import openai
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir une route pour la page d'accueil


@app.route('/')
def home():
    return 'Démarrer la conversation'

# Si vous utilisez le modèle ChatGPT ici, vous pouvez également appeler les fonctions pour interagir avec l'API comme indiqué dans la réponse précédente.


# Démarrer le serveur Flask
if __name__ == '__main__':
    app.run(debug=True)

    # Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API à partir des variables d'environnement
api_key = os.getenv('OPENAI_API_KEY')

# Définir votre clé API
openai.api_key = api_key

# Votre code Flask pour gérer les interactions avec l'interface utilisateur ici
