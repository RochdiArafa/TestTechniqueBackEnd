import flask
from flask import request, jsonify
import sqlite3


app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Base URl = http://127.0.0.1:5000/

@app.route('/', methods=['GET'])
def home():
    return '''<h1>AI Music Play</h1>
<p>c'est le moyen le plus simple pour telecharger les albums , ....</p>'''


# A route to return all of the available entries of Music in our database.
@app.route('/api/musicplay/resources/music/all', methods=['GET'])
def api_music_all():

    #connect à notre base de donnée
    conn = sqlite3.connect('baseDonnees.db')
    cur = conn.cursor()

    #requete pour afficher la liste de music disponible dans notre base de donnée
    cur.execute('SELECT * FROM Music')
    conn.commit()

    liste_Music = cur.fetchall()

    cur.close()
    conn.close()

    # Use the jsonify function from Flask to convert our list
    # to the JSON format.    
    return jsonify(liste_Music)

# A route to return all of the available Album of a specific music in our database.
@app.route('/api/musicplay/resources/album/all', methods=['GET'])
def api_album_all_by_music():
    # Check if an music_id was provided as part of the URL.
    # If music_id is provided, assign it to a variable.
    # If no music_id is provided, display an error in the browser.
    if 'music_id' in request.args:
        music_id = int(request.args['music_id'])
    else:
        return "Erreur: il n'y a pas un music_id au niveau de l'url "

    #connect à notre base de donnée
    conn = sqlite3.connect('baseDonnees.db')
    cur = conn.cursor()

    #requete pour afficher la liste d'Album d'un music disponible dans notre base de donnée
    cur.execute('SELECT * FROM Album where music_id={}'.format(music_id))
    conn.commit()

    liste_Album = cur.fetchall()

    cur.close()
    conn.close()

    # Use the jsonify function from Flask to convert our list
    # to the JSON format.
    return jsonify(liste_Album)      

# Afficher la liste de track d'un album
@app.route('/api/musicplay/resources/album/track/all', methods=['GET'])
def api_track_by_album():
    # Check if an album_id was provided as part of the URL.
    # If album_id is provided, assign it to a variable.
    # If no album_id is provided, display an error in the browser.
    if 'album_id' in request.args:
        album_id = int(request.args['album_id'])
    else:
        return "Erreur: il n'y a pas un album_id au niveau de l'url "

    #connect à notre base de donnée
    conn = sqlite3.connect('baseDonnees.db')
    cur = conn.cursor()
    
    #requete pour afficher la liste de track d'un album disponible dans notre base de donnée
    cur.execute('SELECT * FROM Track where album_id={}'.format(album_id))
    conn.commit()

    liste_Track = cur.fetchall()

    cur.close()
    conn.close()

    # Use the jsonify function from Flask to convert our list
    # to the JSON format.
    return jsonify(liste_Track)  

# Afficher un track à partir d'un lyrics
@app.route('/api/musicplay/resources/track', methods=['GET'])
def api_track_by_lyric():
    # Check if an lyrics was provided as part of the URL.
    # If lyrics is provided, assign it to a variable.
    # If no lyrics is provided, display an error in the browser.
    if 'lyrics' in request.args:
        lyrics = request.args['lyrics']
    else:
        return "Erreur: il n'y a pas un lyrics au niveau de l'url "

    #connect à notre base de donnée
    conn = sqlite3.connect('baseDonnees.db')
    cur = conn.cursor()
    
    #requete pour afficher le track d'un album a partir d'un lyrics disponible dans notre base de donnée
    cur.execute("SELECT * FROM Track where lyrics LIKE '%{}%' ".format(lyrics))
    conn.commit()

    liste_Track = cur.fetchall()

    cur.close()
    conn.close()

    # Use the jsonify function from Flask to convert our list
    # to the JSON format.
    return jsonify(liste_Track) 

app.run()