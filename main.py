#!/usr/bin/env python3
import mysql.connector



db_host = "192.168.230.53" # #_# @IP Serveur MySQL
db_user = "ktr_app_auth"
db_passwd = ""
db_name = "ktr_msc"



# #_# Modification des infos du profile
def edit_profile(name):
	with mysql.connector.connect(host=db_host, user=db_user, password=db_passwd, database=db_name) as sqldb :
		curs = sqldb.cursor()
		req = "SELECT Company, Email, Telephone FROM Profiles WHERE Name = %s"
		val = (name)
		curs.execute(req, val)
		res = curs.fetchall()
		print(f"Nom de la compagnie : {res[0]}")
		company = input("Entrez une nouvelle valeur ou tapez Entrée pour conserver la valeur actuelle : ")
		print(f"Adresse e-mail : {res[1]}")
		email = input("Entrez une nouvelle valeur ou tapez Entrée pour conserver la valeur actuelle : ")
		print(f"Numéro de téléphone : {res[2]}")
		telephone = input("Entrez une nouvelle valeur ou tapez Entrée pour conserver la valeur actuelle : ")
		if company != "":
			req = "UPDATE Profiles SET Company = %s WHERE Name = %s"
			val = (company, name)
			curs.execute(req, val)
			# sqldb.commit()
		if email != "":
			req = "UPDATE Profiles SET Email = %s WHERE Name = %s"
			val = (email, name)
			curs.execute(req, val)
			# sqldb.commit()
		if telephone != "":
			req = "UPDATE Profiles SET Telephone = %s WHERE Name = %s"
			val = (telephone, name)
			curs.execute(req, val)
			# sqldb.commit()
		sqldb.commit()

# #_# Affichage des cartes
def display_cards(owner):
	with mysql.connector.connect(host=db_host, user=db_user, password=db_passwd, database=db_name) as sqldb :
		curs = sqldb.cursor()
		req = "SELECT Name, Company, Email, Telephone FROM Library WHERE Owner = %s"
		val = (owner)
		curs.execute(req, val)
		res = curs.fetchall()
		for elt in res:
			print(elt)

# #_# Création d'une carte
def add_card(owner):
	# #_# On s'assure que le champ obligatoire a été renseigné
	while 1:
		email = input("Adresse mail de la compagnie : ")
		if email == "":
			print("Saisie incorrecte! Veuillez réessayer...")
		else:
			break
	name = input("Nom de la carte : ")
	company= input("Nom de la compagnie : ")
	telephone= input("Numéro de téléphone : ")
	with mysql.connector.connect(host=db_host, user=db_user, password=db_passwd, database=db_name) as sqldb :
		curs = sqldb.cursor()
		req = "INSERT INTO Library (Name, Company, Email, Telephone, Owner) VALUES (%s, %s, %s, %s, %s)"
		val = (name, company, email, telephone, owner)
		curs.execute(req, val)
		sqldb.commit()

# #_# Modification d'une carte
def edit_card(owner):
	with mysql.connector.connect(host=db_host, user=db_user, password=db_passwd, database=db_name) as sqldb :
		curs = sqldb.cursor()
		while 1: #On s'assure que le nom saisi est exact.
			name = input("Entrez le nom de la carte à modifier : ")
			req = "SELECT Company, Email, Telephone, Name FROM Profiles WHERE Name = %s AND Owner = %s"
			val = (name, owner)
			curs.execute(req, val)
			res = curs.fetchall()
			if res != "":
				break
			else:
				print("Carte introuvable!")
		print(f"Nom de la compagnie : {res[0]}")
		company = input("Entrez une nouvelle valeur ou tapez Entrée pour conserver la valeur actuelle : ")
		print(f"Adresse e-mail : {res[1]}")
		email = input("Entrez une nouvelle valeur ou tapez Entrée pour conserver la valeur actuelle : ")
		print(f"Numéro de téléphone : {res[2]}")
		telephone = input("Entrez une nouvelle valeur ou tapez Entrée pour conserver la valeur actuelle : ")
		if company != "":
			req = "UPDATE Library SET Company = %s WHERE Name = %s AND Owner = %s"
			val = (company, name, owner)
			curs.execute(req, val)
			# sqldb.commit()
		if email != "":
			req = "UPDATE Library SET Email = %s WHERE Name = %s AND Owner = %s"
			val = (email, name, owner)
			curs.execute(req, val)
			# sqldb.commit()
		if telephone != "":
			req = "UPDATE Library SET Telephone = %s WHERE Name = %s AND Owner = %s"
			val = (telephone, name, owner)
			curs.execute(req, val)
			# sqldb.commit()
		sqldb.commit()

# #_# Suppression d'une carte
def del_card(owner):
	with mysql.connector.connect(host=db_host, user=db_user, password=db_passwd, database=db_name) as sqldb :
		curs = sqldb.cursor()
		while 1:
			name = input("Entrez le nom de la carte à supprimer : ")
			req = "SELECT Name FROM Profiles WHERE Name = %s AND Owner = %s"
			val = (name, owner)
			curs.execute(req, val)
			res = curs.fetchall()
			if res != "":
				break
			else:
				print("Carte introuvable! Veuillez réessayer avec un autre nom SVP")
		req = "DELETE FROM Library WHERE name = %s AND Owner = %s"
		val = (name, owner)
		curs.execute(req, val)
		sqldb.commit()

def log_out():
	# pass
	logged = False

# #_# Partage de carte avec un autre compte
# def share_card(self, name="", company="", email="", telephone=""):
# 	pass

def run_app(pseudo, logged):
	# Menu après connexion à l'application
	main_options = ["Afficher les cartes", "Ajouter une carte", "Modifier une carte", "Supprimer une carte", "Modifier les informations du profil", "Se déconnecter"]
	while logged == True:
		i = 0

		for opt in main_options:
			i += 1
			print(f"{i} - {opt}")
		print("\n0 - Se déconnecter\n")
		user_req = input("Veuillez choisir une option : ")
		#On s'assure que la saisie est un nombre
		try:
			user_req = int(user_req)
			assert 0 <= user_req <= len(main_options)
		except:
			print("\nSAISIE INCORRECTE ! Veuillez réessayer SVP...\n")
			continue

		if user_req == 1:
			display_cards(pseudo)
		elif user_req == 2:
			add_card(pseudo)
		elif user_req == 3:
			edit_card(pseudo)
		elif user_req == 4:
			del_card(pseudo)
		elif user_req == 5:
			edit_profile(pseudo)
		else:
			log_out()



