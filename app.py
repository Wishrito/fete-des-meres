import os
import random

from flask import Flask, render_template

app = Flask(__name__)

# Données pour le site

mom_quotes = [
    "Une mère est la seule personne au monde qui vous aime avant de vous connaître. – Jean Gastaldi",
    "Le cœur d'une mère est un abîme au fond duquel se trouve toujours un pardon. – Honoré de Balzac",
    "Dieu ne pouvait être partout, alors il a créé les mères. – Proverbe juif",
    "Être mère, c’est découvrir des forces que l’on ignorait posséder. – Linda Wooten",
    "Une maman, c’est une montagne de tendresse dans un océan d’amour.",
    "La main qui berce l’enfant est la main qui domine le monde. – William Ross Wallace",
    "Une mère est celle qui peut prendre la place de tous, mais que personne ne peut remplacer.",
    "Le rôle d'une mère est de créer un monde dans lequel son enfant se sent aimé et capable.",
    "Les bras d'une mère sont faits de tendresse et un enfant y dort profondément. – Victor Hugo",
    "Une mère ne dort jamais vraiment : elle veille avec son cœur.",
]


mom_data = {
    "nom": "Maman",
    "qualites": [
        {
            "adjectif":"Forte",
            "description": "Toujours là pour moi, même dans les moments difficiles.",
        },
        {
            "adjectif":"Intelligente",
            "description": "Tes conseils sont toujours pertinents et pleins de sagesse.",
        },
        {
            "adjectif": "Drôle",
            "description": "Ton humour rend tout plus léger et agréable.",
         },
        {
            "adjectif": "Courageuse",
            "description": "Tu affrontes les défis avec une force incroyable.",
        },
        {
            "adjectif": "Authentique",
            "description": "Tu es toujours toi-même, sans artifice.",
        },
        {
            "adjectif": "Inspirante",
            "description": "Tu me donnes envie de me surpasser et de croire en moi.",
        },
    ],
    "souvenirs": [
        {
            "titre": "Nos discussions du soir",
            "description": "Ces moments où on refait le monde autour d'un bon repas.",
            "annee": "Depuis toujours",
        },
        {
            "titre": "Nos balades et voyages",
            "description": "Les découvertes ensemble, que ce soit près de chez nous ou à l'autre bout de la France.",
            "annee": "Toujours",
        },
        {
            "titre": "Ton soutien dans mes galères",
            "description": "Présente dans les moments difficiles, sans jugement, juste là.",
            "annee": "2020-2024",
        },
        {
            "titre": "Nos fous rires",
            "description": "Ton humour qui détend l'atmosphère et rend tout plus léger.",
            "annee": "En continu",
        },
    ],
    "messages": [
        "Merci d'être restée toi-même malgré tout",
        "Tu m'as appris à être indépendant tout en restant proche",
        "Même si on n'est pas toujours d'accord, je sais que tu veux le meilleur pour moi",
        "Ton soutien compte plus que tu ne le penses",
        "Tu gères ta vie comme une boss",
        "Fier d'être ton fils",
    ],
}

@app.route('/')
def accueil():
    return render_template('accueil.j2', maman=mom_data, citation=random.choice(mom_quotes))

@app.route('/galerie')
def galerie():
    return render_template('galerie.j2', maman=mom_data)

@app.route('/souvenirs')
def souvenirs():
    return render_template('souvenirs.j2', maman=mom_data)

@app.route('/messages')
def messages():
    return render_template('messages.j2', maman=mom_data)

if __name__ == '__main__' and not os.getenv('VERCEL_PRODUCTION_URL'):
    app.run(debug=True)
