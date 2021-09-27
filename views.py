from flask import Flask
from flask import render_template
from flask import request
import sqlite3
app = Flask(__name__)

@app.route("/") 
def index():
    return render_template('accueil.html')

@app.route('/patient', methods=['POST'])
def patient():
    Prenom_v=request.form['Prenom']
    Pin=request.form['Pin']
        
    if Prenom_v=="Admin" and Pin=="Admin":
        texte=render_template('rendu_2.html',Prenom_v="Admin")
    else:
        Erreur="Mauvais Password"
        texte=render_template('accueil.html',Erreur=Erreur)
        
    return(texte)


@app.route('/Admin', methods=['POST'])
def Admin():
    with sqlite3.connect("Patient.db") as con:
        cur = con.cursor()
        Prenom=request.form['CPrenom']
        Nom=request.form['CNom']
        Texte=request.form['CTexte']
        cur.execute("INSERT INTO users(Prenom,Nom,Texte) VALUES(?,?,?)",(Prenom,Nom,Texte))
        
    return(render_template('accueil.html'))



if __name__ == "__main__":
	app.run()