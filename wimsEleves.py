## On part du csv eleves pour obtenir le csv à mettre dans wims

import random

# FONCTIONS UTILES

def generateurmdp(longueur):
	# génère un mot de passe de longueur donné (pas de 0)
	alphanum = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz123456789"
	mdp = ""
	for k in range(longueur):
		lettre = random.choice(alphanum)
		mdp += lettre
		alphanum = alphanum.replace(lettre,"")
	return mdp

def lectureFichier(nomFichier,encodage="UTF-8"):
	# récupère sous forme d'une chaine de caractère le contenu d'un fichier
	contenu = ""
	try:
		file = open(nomFichier,"r",encoding=encodage)
		contenu = file.read()
		file.close()
	except: 
		pass
	return contenu

def ecritureFichier(nomFichier,contenu,encodage="UTF-8"):
	# écrire dans un fichier avec un contenu donné
	status = 0
	try:
		file = open(nomFichier,"w",encoding=encodage)
		contenu = file.write(contenu)
		file.close()
		status = 1
	except: 
		pass
	return status

def caracSpec(nom):
	nom = nom.replace("-","")
	nom = nom.replace("é","e")
	nom = nom.replace("ï","i")
	return nom

def wimsDict(texteEleves):
	# on génère un tableau de dictionnaires pour chaque élèves avec nom,prenom,login,motdepasse
	listeEleves = texteEleves.split("\n")
	dictEleves = []
	for eleve in listeEleves:
		nom = eleve.split(",")[0]
		prenom = eleve.split(",")[1]
		login = caracSpec(nom.lower())
		pswd = generateurmdp(5)
		dictEleves.append({"nom" : nom, "prenom": prenom, "login": login, "password": pswd})
	return dictEleves

def wimsForm(dictEleves):
	# pour un tableau de dictionnaires d'élèves, on génère le csv correspondant
	#file = open("elevesWIMS.csv","w",encoding="UTF-8")
	file = open("elevesWIMS.csv","w",encoding="windows-1252")
	file.write("lastname,firstname,login,password")
	for eleve in dictEleves:
		ligne = f"\n{eleve['nom']},{eleve['prenom']},{eleve['login']},{eleve['password']}"
		file.write(ligne)
	file.close()

# FIN FONCTIONS 

texteEleves = lectureFichier("eleves0.csv","UTF-8")
dictEleves = wimsDict(texteEleves)
wimsForm(dictEleves)