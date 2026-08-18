import string
import secrets

def generer_mot_de_passe (longueur = 16) :
    # 1. Définir les groupe de caractéres indispensables
    minuscules = string.ascii_lowercase
    majuscules = string.ascii_uppercase
    chiffres = string.digits
    symboles = string.punctuation

    # 2. S'assurer d'avoir au moins Un caractére de chaque type pour la sécurité
    mot_de_passe = [
        secrets.choice(minuscules),
        secrets.choice(majuscules),
        secrets.choice(chiffres),
        secrets.choice(symboles)
    ]

    # 3. Remplir le reste de la longueur avec un mélange de tous les carctéres
    tous_les_caracteres = minuscules + majuscules + chiffres + symboles
    for _ in range (longueur - 4):
        mot_de_passe.append(secrets.choice(tous_les_caracteres))

    # 4. Mélanger la liste de maniére sécurisée pour casser l'ordre du début
    secrets.SystemRandom().shuffle(mot_de_passe)

    # 5. Transformer la liste en texte
    return "".join(mot_de_passe)
#--- Exécution du programme ---
print("--- Générateur de mot de passe sécurisée ---")

#Demander le taille à l'utilisateur
taille = int(input("Entrez la longueur du mot de passe (min 8) :"))
if taille < 8 :
    print("Longueur trop court (min 8)")
    taille = 8
mdp_generate = generer_mot_de_passe
print("\nVotre mot de passe sécurisée est :")
print(mdp_generate)        
