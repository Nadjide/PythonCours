# Premier pas de la formation python

"""Nombre = 8.78
NomDePersonne = "Gilbert"
print("{} à fait {} CU/H !".format(NomDePersonne,Nombre))"""

# 2nd Partie

"""CodeTA = input("Quel est votre codeTA ? ")
print("Bienvenue",CodeTA)"""

# 3e partie

"""prixHT = input("Entrez un prix HT :")
prixHT = int(prixHT)
prixTTC = prixHT + (prixHT*20/100)
print("Print TTC =", prixTTC)"""

""""
valeur_booleen = True
valeur_booleen = str(valeur_booleen)
print(valeur_booleen)"""

# Opérations
""""
calcul = 10 / 2
calcul = float(calcul)
calcul2 = 10 % 4
calcul2 = int(calcul2)
print("Résultat =", calcul, "est le reste =", calcul2)
"""

identifiant = "Gael"
mdp = "CTA19"

user_id = input("Quel est votre identifiant ?")
mdp_id = input("Quel est votre mot de passe ? ")

if user_id == identifiant and mdp_id == mdp:
    print("Vous êtes connecté", user_id)
elif user_id != identifiant and mdp_id == mdp:
    print("Identifiant erroné")
elif user_id == identifiant and mdp_id != mdp:
    print("mot de passe est erroné")
else:
    print("Vos informations sont erronées")
