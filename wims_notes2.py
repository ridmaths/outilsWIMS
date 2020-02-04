def arrondi(valeur,p):
    return int(valeur*10**p)/(10**p)

class Eleve:
    """Eleve wims - initialisation avec
        - le nom
        - une liste avec les notes (sous forme de float arrondi à 10-5 près)
    """

    def __init__(self,eleve):
        self.nom = eleve[0].replace('"','')
        notes = eleve[1:]
        for k in range(len(notes)):
            notes[k] = arrondi(float(notes[k]),5)
        self.notes = notes

    def moyenne(self):
        notes = self.notes
        moy=0
        for note in notes:
            moy += note
        return arrondi(moy/3,2)



fichier = open("data.csv","r")
contenu = fichier.read()
fichier.close()

liste_eleves = contenu.split("\n")[3:-1]

eleve = liste_eleves[4].split(",")
# Exemple eleve : eleve = ['"chabane"', '8.3', '5', '0']

print(eleve)
nom = eleve[0]
notes = eleve[1:]

## Execution

el = Eleve(eleve)
print(el.notes)



