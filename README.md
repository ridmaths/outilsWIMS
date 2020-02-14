## Objectifs 

On souhaite automatiser la création d'utilisateurs pour une classe WIMS. 
À partir d'un fichier CSV fourni par pronote, on veut obtenir 

* Générer un mot de passe pour chaque élève
* Obtenir le csv à uploader dans WIMS
* Générer un tex/pdf avec le login et le mot de passe de chaque élève, facile à imprimer / découper / distribuer 

## Détails

# csvPronoteVersWims 

Le programme wimsEleves.py permet de transformer un csv fourni par Python en csv exploitable par wims.

* Le fichier eleves0.csv est le fichier fourni par pronote
* Le fichier elevesWIMS.csv est le fichier obtenu après transformation : celui-ci contient les login/mot de passe des élèves

# documentClasseCodes

Le programme docElevesWims.py permet de générer un document tex/pdf avec les informations de chaque élève. 

On part du fichier elevesWIMS.py généré par le programme précédent et on met en forme le tout.

Les fichiers obtenus à la fin sont listeElevesWims.tex et listeElevesWims.pdf

Les constantes utilisées sont : la classe, le lien du site et le nom du fichier CSV
