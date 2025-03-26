from calculations import addition, soustraction, multiplication, division
from utils import afficher_resultat, valider_nombre

def main():
    print("Bienvenue dans la calculatrice!")
    
    # Demander les nombres à l'utilisateur
    nombre1 = input("Entrez le premier nombre : ")
    nombre2 = input("Entrez le deuxième nombre : ")
    
    # Valider les entrées
    n1 = valider_nombre(nombre1)
    n2 = valider_nombre(nombre2)
    
    if n1 is None or n2 is None:
        return
    
    # Effectuer les calculs
    resultat_addition = addition(n1, n2)
    resultat_soustraction = soustraction(n1, n2)
    resultat_multiplication = multiplication(n1, n2)
    
    try:
        resultat_division = division(n1, n2)
    except ValueError as e:
        print(e)
        return
    
    # Afficher les résultats
    afficher_resultat("l'addition", resultat_addition)
    afficher_resultat("la soustraction", resultat_soustraction)
    afficher_resultat("la multiplication", resultat_multiplication)
    afficher_resultat("la division", resultat_division)

if __name__ == "__main__":
    main()