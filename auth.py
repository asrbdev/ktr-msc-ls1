#!/usr/bin/env python3
import mysql.connector
import hashlib
import main



db_host = "192.168.230.53" #@IP Serveur MySQL
db_user = "ktr_app_auth"
db_passwd = ""
db_name = "ktr_msc"
###############################################################################
try:
	with mysql.connector.connect(host=db_host, user=db_user, password=db_passwd, database=db_name) as sqldb :
		pass
except:
	print("Echec de connexion à la base de données...")
	exit()
###############################################################################
def sign_up():
	print("Création du compte...")

	# #_# Connexion à la base de données
	with mysql.connector.connect(host=db_host, user=db_user, password=db_passwd, database=db_name) as sqldb :
		curs = sqldb.cursor()
		while 1:
			pseudo = input("Veuillez saisir un nom d'utilisateur : ")
			curs.execute(f"SELECT Name FROM Profiles WHERE Name = \"{pseudo}\"")
			res = curs.fetchall()

			# print("Nbre de lignes : ", len(res))
			if len(res) == 0 :
				passwd = input("Veuillez saisir un mot de passe : ")
				# #_# Hashage du mot de passe en MD5
				passwd = hashlib.md5(passwd.encode("utf-8")).hexdigest()
				# curs.execute(f"INSERT INTO Profiles (Name, Secret) VALUES (\"{pseudo}\", \"{passwd}\")")
				req = "INSERT INTO Profiles (Name, Secret) VALUES (%s, %s)"
				val = pseudo, passwd
				curs.execute(req, val)
				break
			else:
				print("Dommage! Ce nom d'utilisateur est déjà pris.")
				continue
		curs.execute("SELECT * FROM Profiles")
		res = curs.fetchall()
		for elt in res:
			print(elt)
		# #_# Enregistrement des modifications
		sqldb.commit()



###############################################################################
def sign_in():
	logged = False
	with mysql.connector.connect(host=db_host, user=db_user, password=db_passwd, database=db_name) as sqldb :
		curs = sqldb.cursor()
		while 1:
			pseudo = input("Veuillez saisir un nom d'utilisateur : ")
			curs.execute(f"SELECT Secret FROM Profiles WHERE Name = \"{pseudo}\"")
			res = curs.fetchall()

			passwd = input("Veuillez saisir un mot de passe : ")
			# #_# Hashage du mot de passe en MD5
			passwd = hashlib.md5(passwd.encode("utf-8")).hexdigest()

			if (res != []) and (passwd == res[0]):
				# Connexion réussie
				main.run_app(logged)
				break
			else:
				print("Identifiants incorrects!")
				continue







