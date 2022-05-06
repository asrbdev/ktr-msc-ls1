#!/usr/bin/env python3
import auth



def main_menu():
	# #_# Menu principal de l'application
	main_options = ["Créer un compte", "Se connecter", "Aide"]
	while 1:
		i = 0

		for opt in main_options:
			i += 1
			print(f"{i} - {opt}")
		print("\n0 - Quitter\n")
		user_req = input("Veuillez choisir une option : ")
		# #_# On s'assure que la saisie est un nombre
		try:
			user_req = int(user_req)
			assert 0 <= user_req <= len(main_options)
		except:
			print("\nSAISIE INCORRECTE ! Veuillez réessayer SVP...\n")
			continue

		if user_req == 1:
			auth.sign_up()
		elif user_req == 2:
			auth.sign_in()
		elif user_req == 3:
			print()
		else: #C'est à dire si user_req == 0
			exit()



if __name__ == "__main__":
	main_menu()
