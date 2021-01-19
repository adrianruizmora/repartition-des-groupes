# La bibliothèque math est importer pour utiliser les fonctions math.ceil et math.floor
import math
import random
import getpass
import json
import time


def logs(message):
    ajouterAuLog = open("logs.txt","a", encoding="utf-8")
    ajouterAuLog.write(message+"\n")


time = time.asctime()
nomDeFichier = input("Veuillez saisir le nom d'un fichier ou son chemin: ")
print(logs("On demande à l'utilisateur de sasir le nom d'un fichier ----> "+ "Nom d'utilisateur active : " +getpass.getuser()+" ----> " + " Date : " +str(time)))
maxPersonnesParGroupe = int(input("nb de personnes max par groupe: "))
print(logs("On demande à l'utilisateur de saisir un max par groupe ---->"+ "Nom d'utilisateur active : " +getpass.getuser()+" ----> " + " Date : " +str(time)))
listeDeNoms = open(nomDeFichier,"r",encoding="utf-8")
lignes = listeDeNoms.readlines()



def groupes(lignes,maxPersonnesParGroupe):
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
    print(logs("On creer une liste avec le nombre des personnes par groupe --->"+ "Nom d'utilisateur active : " +getpass.getuser()+" ----> " + " Date : " +str(time)))
    return membresParGroupe


def nomAleatoire(lignes): 
    indexAleatoire = random.randrange(len(lignes))
    nom = lignes[indexAleatoire]
    print(logs("On sort un nom aleatoire de notre fichier ---->"+ "Nom d'utilisateur active : " +getpass.getuser()+" ----> " + " Date : " +str(time)))
    return nom

def listeDeNomAleatoire(membresParGroupe, lignes):
    listeParGroupe =[]

    for i in range(membresParGroupe):
        nom = nomAleatoire(lignes)
        if listeParGroupe.count(nom) == 0:
            listeParGroupe.extend([nom])
            lignes.remove(nom)
    print(logs("On cree une liste des groupes avec des noms aleatoire ---->"+ "Nom d'utilisateur active : " +getpass.getuser()+" ----> " + " Date : " +str(time)))
    return listeParGroupe

dico_groupes = {}
groupes = groupes(lignes, maxPersonnesParGroupe)
nbDesGroupes = 1


def creerFichierDesGroupes(groupes,nbDesGroupes):
    print(logs("On creer un fichier avec les groupes ---->"+ "Nom d'utilisateur active : " +getpass.getuser()+" ----> " + " Date : " +str(time)))
    nouveauFichier= open("groupes.txt","w+",encoding="utf-8")
    listeDesGroupes = []
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
   
    
def fichier_json(dico_groupes):
    with open("data_file.json", "w", encoding="utf-8") as write_file:
        json.dump(dico_groupes, write_file, ensure_ascii=False)
        return(write_file)

creerFichierDesGroupes(groupes,nbDesGroupes)
log("")
fichier_json(dico_groupes)
