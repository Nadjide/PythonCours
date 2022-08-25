#Exercice en python


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