import math
import random
import getpass
import json
import time

time = time.asctime()

def logs(message):
    ajouterAuLog = open("logs.txt","a", encoding="utf-8")
    ajouterAuLog.write(message+ " ----> Nom d'utilisateur active : " +getpass.getuser()+" ----> " + " Date : " +str(time)+"\n")
    return message

def listeDesGroupes(lignes,maxPersonnesParGroupe):
    nbPersonnesDansFichier = len(lignes)
    nbDesGroupes = math.ceil(nbPersonnesDansFichier/maxPersonnesParGroupe)
    nbDesPeronnesParGroupe = math.floor(nbPersonnesDansFichier/nbDesGroupes)
    membresParGroupe = []
    nbDesPersonnesRestantes = nbPersonnesDansFichier%nbDesGroupes

    for i in range(nbDesGroupes):
        if nbDesPersonnesRestantes>0:
            membresParGroupe.extend([nbDesPeronnesParGroupe+1])
            nbDesPersonnesRestantes -= 1
        else:
            membresParGroupe.extend([nbDesPeronnesParGroupe])
    logs("On creer une liste avec le nombre des personnes par groupe")
    return membresParGroupe

def nomAleatoire(lignes): 
    indexAleatoire = random.randrange(len(lignes))
    nom = lignes[indexAleatoire]
    logs("On sort un nom aleatoire de notre fichier")
    return nom

def listeDeNomAleatoire(membresParGroupe, lignes):
    listeParGroupe =[]

    for i in range(membresParGroupe):
        nom = nomAleatoire(lignes)
        if listeParGroupe.count(nom) == 0:
            listeParGroupe.extend([nom])
            lignes.remove(nom)
    logs("On cree une liste des groupes avec des noms aleatoire")
    return listeParGroupe

def fichierDesGroupes(groupes,lignes):
    logs("On creer un fichier avec les groupes")
    nouveauFichier= open("groupes.txt","w+",encoding="utf-8")
    listeDesGroupes = []
    dico_groupes = {} 
    nbDesGroupes = 1
    for nbParGroupe in groupes:
            if nbDesGroupes <= len(groupes)+1:
                nouveauFichier.write("Groupe #" + str(nbDesGroupes)+"\n")
                nbDesGroupes +=1
                for nom in listeDeNomAleatoire(nbParGroupe,lignes):
                    listeDesGroupes.extend([nom.strip()])
                    nouveauFichier.write(nom + "\n".strip())
                dico_groupes["Groupe #"+ str(nbDesGroupes-1)] = listeDesGroupes
                listeDesGroupes = []
            nouveauFichier.write("\n")
    nouveauFichier.close()
    return dico_groupes
   
def fichier_json(dico_groupes):
    with open("data_file.json", "w", encoding="utf-8") as write_file:
        json.dump(dico_groupes, write_file, ensure_ascii=False)
        return(write_file)

def fichiers(nomDuFichier,nbMaxPersonnesParGroupe):
    listeDeNoms = open(nomDuFichier,"r",encoding="utf-8")
    lignes = listeDeNoms.readlines()
    groupes = listeDesGroupes(lignes,nbMaxPersonnesParGroupe)
    fichier_json(fichierDesGroupes(groupes,lignes))
    logs("Fichier texte avec des groupes crée correctement")
    logs("Fichier Json crée correctement")
    logs("Fichier texte des logs crée correctement")

if __name__ == "__main__":
    import sys
    fichiers(sys.argv[1], int(sys.argv[2]))
     