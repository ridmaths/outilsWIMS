import os

# Pas de fonctions ! 

# Des constantes :

nomFichier = "elevesWIMS.csv"
lienWims = "liendusite"
classe = "Seconde 12"

## On récupère les données élève sous forme de dictionnaire

fichier = open(nomFichier,"r",encoding="windows-1252")
#fichier = open(nomFichier,"r",encoding="UTF-8")
texte = fichier.read()

dataEleves = texte.split("\n")[1:]
dictEleves = []

for eleve in dataEleves:
	login = eleve.split(",")[2]
	password = eleve.split(",")[3]
	dictEleves.append({"login": login, "password": password})

# On obtient alors un dictionnaire avec les données de chaque élève (login et password)


## On génère le contenu

contenu = ""
for obj in dictEleves:
	contenu += f'''\\fbox{{\\begin{{minipage}}{{0.9\\linewidth}}
\\textbf{{Plateforme WIMS}}

\\medskip

Pour accéder à la classe virtuelle, ouvrir un navigateur web et entrer l'adresse suivante : \\par 
{lienWims}

\\medskip

Voici vos identifiants pour vous connecter :

\\medskip

\\textbf{{Pseudo : }} {obj['login']} 

\\medskip

\\textbf{{Mot de passe : }} {obj['password']}
\\end{{minipage}}}}

\\vspace{{1cm}}
'''

## FIN CONTENU


## On construit le document latex correspondant

document = '''\\documentclass[12pt,a4paper]{article} 
  
\\usepackage[utf8]{inputenc} 
\\usepackage[french]{babel} 
\\usepackage[T1]{fontenc} 
\\usepackage{fourier} 
\\usepackage{amsmath,amsfonts,amssymb} 
\\usepackage[left=1cm,right=1cm,top=1cm,bottom=0.5cm]{geometry} 
\\usepackage{xcolor} 
\\usepackage{multicol}
 
\\setlength\\parindent{0mm} 
 
\\begin{document}

\\begin{center} \\large \\textbf{Liste des élèves pour WIMS - '''+classe+'''} \\end{center}

\\bigskip

\\begin{multicols}{2}

'''

document += contenu

document += '''
\\end{multicols}
\\end{document}'''

## FIN DOCUMENT

## On construit le fichier .tex et le .pdf

nomLatex = "listeElevesWims"
fichier = open(nomLatex+".tex","w",encoding="UTF-8")
fichier.write(document)
fichier.close()

commande = f"pdflatex -quiet {nomLatex}.tex"
os.system(commande)

# On obtient le pdf, puis on enleève les fichiers inutiles pour la suite

os.system(f"del {nomLatex}.aux")
os.system(f"del {nomLatex}.log")