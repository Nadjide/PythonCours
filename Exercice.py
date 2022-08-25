#Exercice 1 en python

"""
id_user = input("Nom d'utilisateur ?")
mdp_user = input("Votre mot de passe ?")

print("Bienvenue",id_user," vous êtes à présent connecté")

besoin = input("Avez vous besoin de calculer quelque chose ?")

if besoin == "oui" or besoin == "Oui":
    nb1 = int(input("Nombre 1 :"))
    nb2 = int(input("Nombre 2 :"))
    operation = input("operateur ?")
    if operation == "+":
        resultat = int(nb1+nb2)
        print(resultat)
    elif operation == "-":
        resultat = int(nb1-nb2)
        print(resultat)
    elif operation == "*" or operation == "x":
        resultat = int(nb1*nb2)
        print(resultat)
    elif operation == "/":
        resultat = float(nb1/nb2)
        print(resultat)
    else:print("Veuillez choisir un opérateur valide !")
else:print("D'accord vous allez être deconnecté", id_user," au revoir !")
"""

#boucle while
import time

jeu = input("Voulez vous lancer  Asphlat 7 ?")
if jeu=="oui" or jeu=="Oui":
    print("Le jeu démarre ..")
    time.sleep(5)
    print("Bonne session :)")
    time.sleep(5)
    while jeu:
        choix = input("Voulez vous continuer à jouer ?")
        if choix == "oui":
            continue
        elif choix == "non" or choix == "Non":
            print("le jeu est stoppé")
            break
        elif choix == "pause":
            print("Le jeu est en pause !")
            time.sleep(5)
            while choix:
                pause = input("voulez vous sortir de la pause ?")
                if pause == "oui":
                    print("bonne session")
                    time.sleep(5)
                    break
                else:
                    time.sleep(3)
                    continue
else:print("Le jeu n'a pas démarrer")


