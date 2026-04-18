from flask import Flask
import random

app = Flask(__name__)

list_of_facts = [
    "Undertale foi criado em 2015",
    "Pessoas nascidas em 1965 tem 61 anos em 2026",
    "Na história original de Ariel, sua língua é cortada fora em vez da garota perder a voz",
    "Pessoas nascidas em 2010 poderam chegar a 2100, se viverem até os 90 anos de idade"
]

@app.route("/")
def home():
    return "Está é a página inicial."

@app.route("/random_facts")
def facts():
    return f"""
    <html>
        <head>
            <title>Fatos aleatórios que eu sei</title>
        </head>
        <body>
            <h1>Fato aleatório</h1>
            <p>{random.choice(list_of_facts)}</p>
            <p>Atualize a página para receber um novo fato!</p>
        </body>
    </html>
"""

if __name__ == "__main__":
    app.run(debug=True)

