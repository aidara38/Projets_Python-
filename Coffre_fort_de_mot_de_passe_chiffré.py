coffre = {}
def ajout():
    global coffre

    nom_site = input("Veillez saisir le nom du site :")
    mdp_site = input("Veillez saisir le mot de passe associé à ce site :")
    coffre[nom_site] = mdp_site
    print(f"Mot de passe pour {coffre[nom_site]} ajouté avec succés")
def affiche():
        global coffre

        if not coffre :
           print("Pas de mot de passe")
        else :
            for cle, valeur in coffre.items() :
                print(f"Mot de passe pour {cle} : {valeur}")        
while True :
    print(f"1- Ajouter un mot de passe \n2- Afficher les mots de passe \n3- Quitter le prgramme")
    choix = int(input("Veillez faire votre choix :"))
    if choix == 1 :
        ajout()
    elif choix == 2 :
        affiche()
    elif choix == 3 :
        break
    else :
        print("Choix invalide réesseyée !")

