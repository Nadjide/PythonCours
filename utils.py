def afficher_resultat(operation, resultat):
    print(f"Le résultat de {operation} est : {resultat}")

def valider_nombre(nombre):
    try:
        return float(nombre)
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide")
        return None