import sqlite3

conn = sqlite3.connect('baseDonnees.db')
cur = conn.cursor()

#requete sql pour creer la table Music
cur.execute("CREATE TABLE IF NOT EXISTS Music(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, type TEXT)")

#requete sql pour inserer des donnée dans la table Music
cur.execute("INSERT INTO Music(id,type) VALUES(0,'Soul music')")
cur.execute("INSERT INTO Music(id,type) VALUES(1,'Disco music')")
cur.execute("INSERT INTO Music(id,type) VALUES(2,'Arabic music')")
cur.execute("INSERT INTO Music(id,type) VALUES(3,'Romantic music')")


#requete sql pour creer la table Album
cur.execute("CREATE TABLE IF NOT EXISTS Album(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, music_id INTEGER)")

#requete sql pour inserer des donnée dans la table Album
cur.execute("INSERT INTO Album(id,nom,music_id) VALUES(0,'Where do we go from here',1)")
cur.execute("INSERT INTO Album(id,nom,music_id) VALUES(1,'wake Up Love',1)")
cur.execute("INSERT INTO Album(id,nom,music_id) VALUES(2,'Pelota',1)")
cur.execute("INSERT INTO Album(id,nom,music_id) VALUES(3,'Soulful I need that in my life',1)")
cur.execute("INSERT INTO Album(id,nom,music_id) VALUES(4,'Where Do We Go From Here?',2)")

#requete sql pour creer la table Track
cur.execute("CREATE TABLE IF NOT EXISTS Track(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, nom TEXT, image TEXT, lien_audio TEXT, lyrics TEXT, album_id INTEGER)")

#requete sql pour inserer des donnée dans la table Track
cur.execute("INSERT INTO Track(id,nom,image,lien_audio,lyrics, album_id) VALUES(0,'Track 1','https://www.aviationanalysis.net/wp-content/uploads/2020/09/BLACKPINK-reveals-The-Album-title-track.jpg','http://www.songsify.com/english/general-admission_machine-gun-kelly_2015.html','https://www.azlyrics.com/m/machinegunkelly.html#86257',1)")
cur.execute("INSERT INTO Track(id,nom,image,lien_audio,lyrics, album_id) VALUES(1,'Track 2','https://www.aviationanalysis.net/wp-content/uploads/2020/09/BLACKPINK-reveals-The-Album-title-track.jpg','http://www.songsify.com/english/general-admission_machine-gun-kelly_2015.html','https://www.azlyrics.com/m/machinegunkelly.html#86257',1)")
cur.execute("INSERT INTO Track(id,nom,image,lien_audio,lyrics, album_id) VALUES(2,'Track 3','https://www.aviationanalysis.net/wp-content/uploads/2020/09/BLACKPINK-reveals-The-Album-title-track.jpg','http://www.songsify.com/english/general-admission_machine-gun-kelly_2015.html','Je taime comme un fout',1)")
cur.execute("INSERT INTO Track(id,nom,image,lien_audio,lyrics, album_id) VALUES(3,'Track 4','https://www.aviationanalysis.net/wp-content/uploads/2020/09/BLACKPINK-reveals-The-Album-title-track.jpg','http://www.songsify.com/english/general-admission_machine-gun-kelly_2015.html','si tu savais comme bien je taime',2)")
cur.execute("INSERT INTO Track(id,nom,image,lien_audio,lyrics, album_id) VALUES(4,'Track 5','https://www.aviationanalysis.net/wp-content/uploads/2020/09/BLACKPINK-reveals-The-Album-title-track.jpg','http://www.songsify.com/english/general-admission_machine-gun-kelly_2015.html','https://www.azlyrics.com/m/machinegunkelly.html#86257',1)")


conn.commit()

cur.close()
conn.close()